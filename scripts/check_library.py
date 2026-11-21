#!/usr/bin/env python3
"""Check that the pattern library holds no source identifiers.

The checker fails on a Source note or a web address in a library file.
"""

import argparse
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).parents[1]
URL = re.compile(r"\b(?:https?|ftp)://\S+|\bwww\.\S+", re.IGNORECASE)
SOURCE = re.compile(r"(?<![a-z])source\s*:", re.IGNORECASE)
TAG = re.compile(r"<[^>]*>")
MARKUP = str.maketrans("", "", "*_~")


def has_source_note(text):
    """Return True when text holds a Source note, in plain text or markup.

    The first match catches a note inside an HTML comment, which tag
    removal would otherwise delete. The second match strips HTML tags
    and Markdown emphasis characters before matching.
    """
    if SOURCE.search(text):
        return True
    plain = TAG.sub("", text).translate(MARKUP)
    return bool(SOURCE.search(plain))


def check_file(path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [f"{path}: invalid encoding"]
    findings = []
    if has_source_note(text):
        findings.append(f"{path}: Source line")
    if URL.search(text):
        findings.append(f"{path}: web address")
    return findings


def check_tree(root):
    findings = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            findings.extend(check_file(path))
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", help="library directory to check instead of the repository one")
    args = parser.parse_args(argv)
    findings = check_tree(pathlib.Path(args.root) if args.root else ROOT / "library")
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
