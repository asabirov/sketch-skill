#!/usr/bin/env python3
"""Regenerate the README example and the visual library pictures.

Usage, from the repository root:

    python3 docs/render.py                 # assets/preview.png, every thumbnail, docs/templates.md
    python3 docs/render.py --preview-only  # only assets/preview.png
    python3 docs/render.py --library-only  # only the thumbnails and docs/templates.md

Requirements: Python 3 with Pillow, and the `agent-browser` CLI in PATH.
The script inlines the kit, embeds the Geist font, captures each page with
agent-browser's headless Chrome, and reduces each library thumbnail to 16 colours.
"""

import base64
import functools
import hashlib
import http.server
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.request

REPO = pathlib.Path(__file__).resolve().parent.parent
AGENT_BROWSER = shutil.which("agent-browser")
FONT_URL = "https://cdn.jsdelivr.net/npm/geist@1.3.1/dist/fonts/geist-sans/Geist-Variable.woff2"
FONT_SHA256 = "28258d0621216948416a859d32487ab6ad1c9effa0d08795698e70be3c917630"

# The order of the categories in the README "Template categories" table.
CATEGORY_ORDER = [
    "app-shell", "home", "conversation", "list", "catalog", "projects",
    "project", "search", "menu", "settings", "landing", "notes", "detail",
    "form", "dashboard", "chart", "board", "checkout", "pricing", "sign-in",
    "onboarding", "empty", "mobile",
]

# Wait for the page and every same-origin iframe to finish loading and fonts.
READY_JS = (
    "[document, ...[...document.querySelectorAll('iframe')].map(f => f.contentDocument)]"
    ".every(d => d && d.readyState === 'complete' && d.fonts.status === 'loaded')"
)


def run(*args):
    subprocess.run(list(args), check=True, capture_output=True, text=True)


def get_font():
    """Return the Geist font bytes, or None when it cannot be fetched.

    The kit names Geist first in its font stack. A host without Geist draws the
    fallback font, so the pictures would differ between hosts. Cache the file
    under ~/.cache/sketch-skill/ so a later run works offline.
    """
    cache = pathlib.Path.home() / ".cache" / "sketch-skill"
    cache.mkdir(parents=True, exist_ok=True)
    target = cache / "Geist-Variable.woff2"
    if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == FONT_SHA256:
        return target.read_bytes()
    try:
        with urllib.request.urlopen(FONT_URL, timeout=30) as response:
            data = response.read()
    except Exception as exc:
        print(f"render: cannot fetch the Geist font ({exc}); the pictures use the fallback font", file=sys.stderr)
        return None
    if hashlib.sha256(data).hexdigest() != FONT_SHA256:
        print("render: the fetched Geist font has the wrong hash; the pictures use the fallback font", file=sys.stderr)
        return None
    tmp = target.with_suffix(".tmp")
    tmp.write_bytes(data)
    tmp.replace(target)
    return data


def build(source, font):
    """Print a page as one file: the kit inlined and the Geist font embedded."""
    page = subprocess.run(
        [sys.executable, str(REPO / "assets" / "sketch_inline.py"), str(source)],
        check=True, capture_output=True, text=True,
    ).stdout
    if font:
        font_b64 = base64.b64encode(font).decode()
        face = (
            '<style>@font-face { font-family: Geist; font-weight: 100 900; '
            f'src: url(data:font/woff2;base64,{font_b64}) format("woff2"); }}</style>\n'
        )
        head, mark, rest = page.partition("<title>")
        if not mark:
            sys.exit(f"render: {source} has no <title>")
        page = head + face + mark + rest
    return page


def start_server(directory):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(directory))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, server.server_address[1]


def shoot(port, path, width, height, scale, out):
    """Capture one page as a PNG at the given viewport size and device scale."""
    url = f"http://127.0.0.1:{port}/{path}?theme=light"
    run(AGENT_BROWSER, "--session", "sketch-render", "set", "viewport", str(width), str(height), str(scale))
    run(AGENT_BROWSER, "--session", "sketch-render", "open", url)
    run(AGENT_BROWSER, "--session", "sketch-render", "wait", "--fn", READY_JS)
    run(AGENT_BROWSER, "--session", "sketch-render", "screenshot", str(out))


def shrink(folder):
    """Reduce each PNG under folder to 16 colours, in place."""
    from PIL import Image
    for path in sorted(pathlib.Path(folder).rglob("*.png")):
        Image.open(path).convert("RGB").quantize(16, dither=Image.Dither.NONE).save(path, optimize=True)


def template_rows(folder):
    """Return the markdown rows for one category folder, sorted by file name."""
    rows = []
    for page in sorted(folder.glob("*.html")):
        text = page.read_text()
        category, name = re.search(r"<title>(.*?): (.*?)</title>", text).groups()
        best_for = re.match(r"<!-- Best for: (.*?) -->", text).group(1)
        path = f"{folder.name}/{page.stem}"
        rows.append(
            "<tr>\n"
            f'<td width="460"><a href="templates/{path}.png"><img src="templates/{path}.png" width="440" alt="{category}: {name}"></a></td>\n'
            f'<td><b>{name}</b><br>{best_for}<br><a href="../templates/{path}.html"><code>templates/{path}.html</code></a></td>\n'
            "</tr>"
        )
    return rows


def make_templates_md():
    """Write the full docs/templates.md, in README table order."""
    root = REPO / "templates"
    folders = [root / name for name in CATEGORY_ORDER]
    total = sum(len(list(p.glob("*.html"))) for p in folders)
    sections = []
    for folder in folders:
        rows = template_rows(folder)
        category = re.search(r"<title>(.*?): (.*?)</title>", sorted(folder.glob("*.html"))[0].read_text()).group(1)
        sections.append((category, rows))

    lines = ["# Templates", ""]
    lines.append(
        f"The skill has {total} page templates in {len(CATEGORY_ORDER)} categories. "
        "Copy the file at the path of an entry to start a sketch. A click on a picture opens it at its full size."
    )
    lines.append("")
    lines.append(
        "Run `python3 docs/render.py` from the repository root to refresh these pictures after a template changes. "
        "It needs Python 3 with Pillow and the `agent-browser` CLI."
    )
    lines.append("")
    lines.append(", ".join(f"[{c}](#{c.lower().replace(' ', '-')})" for c, _ in sections))
    lines.append("")
    for category, rows in sections:
        lines.append(f"## {category}")
        lines.append("")
        lines.append("<table>")
        lines.extend(rows)
        lines.append("</table>")
        lines.append("")
    (REPO / "docs" / "templates.md").write_text("\n".join(lines))


def main():
    args = sys.argv[1:]
    preview_only = "--preview-only" in args
    library_only = "--library-only" in args
    if preview_only and library_only:
        sys.exit("render: pass only one of --preview-only and --library-only")
    unknown = [a for a in args if a not in ("--preview-only", "--library-only")]
    if unknown:
        sys.exit("render: unknown argument: " + unknown[0])

    font = get_font()
    work = pathlib.Path(tempfile.mkdtemp(prefix="sketch-render-"))
    try:
        if preview_only:
            (work / "built").mkdir()
            for name in ("chat-with-files", "plans", "phone-inbox", "launch-board"):
                (work / "built" / f"{name}.html").write_text(build(REPO / "docs" / "examples" / f"{name}.html", font))
            (work / "readme-option-b.html").write_text(build(REPO / "docs" / "examples" / "readme-option-b.html", font))
            server, port = start_server(work)
            try:
                shoot(port, "readme-option-b.html", 1280, 800, 2, REPO / "assets" / "preview.png")
            finally:
                server.shutdown()
                server.server_close()
        else:
            # The README example is one canvas with four example screens in iframes.
            if not library_only:
                (work / "built").mkdir()
                for name in ("chat-with-files", "plans", "phone-inbox", "launch-board"):
                    (work / "built" / f"{name}.html").write_text(build(REPO / "docs" / "examples" / f"{name}.html", font))
                (work / "readme-option-b.html").write_text(build(REPO / "docs" / "examples" / "readme-option-b.html", font))

            # Each template becomes one self-contained page.
            templates = []
            for category in CATEGORY_ORDER:
                for page in sorted((REPO / "templates" / category).glob("*.html")):
                    built = work / f"templates--{category}--{page.stem}.html"
                    built.write_text(build(page, font))
                    templates.append((category, page.stem, built))

            server, port = start_server(work)
            try:
                if not library_only:
                    shoot(port, "readme-option-b.html", 1280, 800, 2, REPO / "assets" / "preview.png")
                for category, name, built in templates:
                    out = REPO / "docs" / "templates" / category
                    out.mkdir(parents=True, exist_ok=True)
                    shoot(port, built.name, 1024, 640, 1, out / f"{name}.png")
            finally:
                server.shutdown()
                server.server_close()
    finally:
        try:
            run(AGENT_BROWSER, "--session", "sketch-render", "close")
        except subprocess.CalledProcessError:
            pass
        shutil.rmtree(work, ignore_errors=True)

    if not preview_only:
        shrink(REPO / "docs" / "templates")
        make_templates_md()


if __name__ == "__main__":
    if not AGENT_BROWSER:
        sys.exit("render: the agent-browser CLI is not in PATH")
    main()
