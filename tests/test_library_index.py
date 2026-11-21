import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).parents[1]
LIBRARY = ROOT / "library"


class LibraryIndexTest(unittest.TestCase):
    def setUp(self):
        self.patterns = sorted(f"{p.parent.parent.name}/{p.parent.name}" for p in LIBRARY.glob("*/*/pattern.md"))
        self.categories = sorted({p.split("/")[0] for p in self.patterns})

    def test_index_lists_each_pattern(self):
        index = (ROOT / "docs" / "library.md").read_text(encoding="utf-8")
        listed = sorted(re.findall(r"\]\(\.\./library/([\w-]+/[\w-]+)/\)", index))
        self.assertEqual(listed, self.patterns)

    def test_counts_match(self):
        sentence = f"The library has {len(self.patterns)} patterns in {len(self.categories)} categories."
        for doc in ("docs/library.md", "README.md"):
            with self.subTest(doc=doc):
                self.assertIn(sentence, (ROOT / doc).read_text(encoding="utf-8"))

    def test_readme_counts_each_category(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        section = readme.split("## Pattern library", 1)[1].split("\n## ", 1)[0]
        rows = dict(re.findall(r"^\| ([A-Z][\w ]*) \| (\d+) \|", section, re.M))
        expected = {c.capitalize(): str(sum(1 for p in self.patterns if p.startswith(f"{c}/"))) for c in self.categories}
        self.assertEqual(rows, expected)


if __name__ == "__main__":
    unittest.main()
