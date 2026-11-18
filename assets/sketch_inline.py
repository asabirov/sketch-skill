#!/usr/bin/env python3
"""Print a sketch page as one file that holds the current kit and its version.

Usage: python3 "<skill-folder>/assets/sketch_inline.py" page.html > sketch.html
Write the page with links to assets/sketch.css and assets/sketch.js,
or run it on a page that already holds an inlined kit. Each inlined block carries
data-sketch-kit="<version>". The version is read from metadata.version in SKILL.md. The kit is
read from this script's own folder, so the page never carries a copy of it.
"""
import pathlib
import re
import sys

here = pathlib.Path(__file__).resolve().parent
version_match = re.search(r'^\s*version:\s*"([^"]+)"', (here.parent / "SKILL.md").read_text(), re.M)
if not version_match:
    sys.exit("sketch_inline: no metadata.version in SKILL.md")
version = version_match.group(1)
css = (here / "sketch.css").read_text()
js = (here / "sketch.js").read_text()
css_head = css.lstrip().split("\n", 1)[0].strip()
js_head = js.lstrip().split("\n", 1)[0].strip()

style_block = f'<style data-sketch-kit="{version}">\n{css}</style>'
script_block = f'<script data-sketch-kit="{version}">\n{js}</script>'

if len(sys.argv) != 2:
    sys.exit('Usage: python3 "<skill-folder>/assets/sketch_inline.py" page.html > sketch.html')
page = pathlib.Path(sys.argv[1]).read_text()

link = re.compile(r'<link\b[^>]*href="(?:(?:\.\./)*assets/)?sketch\.css"[^>]*>')
script_link = re.compile(r'<script\b[^>]*src="(?:(?:\.\./)*assets/)?sketch\.js"[^>]*>\s*</script>')
marked_style = re.compile(r'<style\b[^>]*data-sketch-kit="[^"]*"[^>]*>.*?</style>', re.S)
marked_script = re.compile(r'<script\b[^>]*data-sketch-kit="[^"]*"[^>]*>.*?</script>', re.S)
unmarked_style = re.compile(r'<style\b([^>]*)>(.*?)</style>', re.S)
unmarked_script = re.compile(r'<script\b([^>]*)>(.*?)</script>', re.S)


def is_inlined_css(match):
    return match.group(2).lstrip().startswith(css_head)


def is_inlined_js(match):
    return match.group(2).lstrip().startswith(js_head)


has_css = bool(
    link.search(page)
    or marked_style.search(page)
    or any(is_inlined_css(m) for m in unmarked_style.finditer(page))
)
has_js = bool(
    script_link.search(page)
    or marked_script.search(page)
    or any(is_inlined_js(m) for m in unmarked_script.finditer(page))
)
if not (has_css and has_js):
    sys.exit("sketch_inline: the page needs links to assets/sketch.css and assets/sketch.js, or an inlined kit")

page = link.sub(lambda _: style_block, page)
page = script_link.sub(lambda _: script_block, page)
page = marked_style.sub(lambda _: style_block, page)
page = marked_script.sub(lambda _: script_block, page)
page = unmarked_style.sub(lambda m: style_block if is_inlined_css(m) else m.group(0), page)
page = unmarked_script.sub(lambda m: script_block if is_inlined_js(m) else m.group(0), page)
sys.stdout.write(page)
