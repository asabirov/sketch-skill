import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class SketchFactsTest(unittest.TestCase):
    def setUp(self):
        self.css = (ROOT / "assets" / "sketch.css").read_text(encoding="utf-8")

    def test_label_centres_only_beside_a_control(self):
        self.assertRegex(
            self.css,
            r"\.sketch-facts dt:has\(\+ dd > :is\(\.sketch-switch, button, input, select\)\) \{ align-self: center",
        )

    def test_facts_rule_does_not_centre_every_row(self):
        self.assertNotRegex(self.css, r"\.sketch-facts \{ [^}]*align-items: center")
        self.assertNotRegex(self.css, r"\.sketch-facts-share \{ [^}]*align-items: center")

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
