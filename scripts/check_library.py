#!/usr/bin/env python3
"""Check that the pattern library contains no source identifiers.

The checker uses SHA-256 hashes of case-folded, space-normalized names.
"""

import argparse
import hashlib
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).parents[1]
HASH_FILE = ROOT / "scripts" / "library_name_hashes.json"
URL = re.compile(r"\b(?:https?|ftp)://\S+|\bwww\.\S+", re.IGNORECASE)
SOURCE = re.compile(r"^\s*source\s*:", re.IGNORECASE | re.MULTILINE)
WORDS = re.compile(r"[\w]+(?:['’-][\w]+)*", re.UNICODE)


def normalize_name(value):
    return " ".join(value.casefold().split())


def hash_name(value):
    return hashlib.sha256(normalize_name(value).encode("utf-8")).hexdigest()


def phrases(text):
    words = WORDS.findall(text)
    for start in range(len(words)):
        for length in range(1, min(4, len(words) - start) + 1):
            yield " ".join(words[start : start + length])


def check_file(path, hashes):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    findings = []
    if SOURCE.search(text):
        findings.append(f"{path}: Source line")
    if URL.search(text):
        findings.append(f"{path}: web address")
    if any(hash_name(phrase) in hashes for phrase in phrases(text)):
        findings.append(f"{path}: blocked name")
    return findings


def check_tree(root, hashes):
    findings = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            findings.extend(check_file(path, hashes))
    return findings


def load_hashes():
    return set(json.loads(HASH_FILE.read_text(encoding="utf-8")))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--hash", action="store_true", help="hash names from standard input")
    args = parser.parse_args(argv)
    if args.hash:
        for line in sys.stdin:
            print(hash_name(line))
        return 0
    findings = check_tree(ROOT / "library", load_hashes())
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
