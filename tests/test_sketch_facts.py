import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class SketchFactsTest(unittest.TestCase):
    def setUp(self):
        self.css = (ROOT / "assets" / "sketch.css").read_text(encoding="utf-8")

    def test_each_fact_row_centres_its_label(self):
        self.assertRegex(self.css, r"\.sketch-facts \{ [^}]*align-items: center")

    def test_share_wrapper_has_one_label_column(self):
        self.assertRegex(
            self.css,
            r"\.sketch-facts-share \{ [^}]*grid-template-columns: max-content minmax\(0, 1fr\)",
        )
        self.assertRegex(self.css, r"\.sketch-facts-share > \.sketch-facts \{ display: contents")

    def test_prototypes_name_the_share_option(self):
        proto = (ROOT / "references" / "sketch-prototypes.md").read_text(encoding="utf-8")
        self.assertIn("sketch-facts-share", proto)


if __name__ == "__main__":
    unittest.main()
