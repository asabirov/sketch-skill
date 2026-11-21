import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).parents[1]
CONTENT = ROOT / "library" / "content"

# Each catalog pattern is its own folder and renders one fixed variation.
EXPECTED = {
    "catalog-base-view": "base",
    "catalog-display-panel": "display-panel",
    "catalog-side-list": "side-list",
    "catalog-tabs": "view-tabs",
}


class CatalogVariationTests(unittest.TestCase):
    def text_for(self, name):
        return (CONTENT / name / "sketch.html").read_text(encoding="utf-8")

    def test_each_catalog_pattern_renders_its_own_variation(self):
        for name, variation in EXPECTED.items():
            with self.subTest(name=name):
                text = self.text_for(name)
                html_tag = re.search(r"<html\b[^>]*>", text).group(0)
                self.assertIn(f'data-variation="{variation}"', html_tag)
                # The load call keeps the file's own variation. It reads no query
                # parameter and no removed variation button can push it to base.
                self.assertIn("set_variation(document.documentElement.dataset.variation);", text)
                self.assertNotIn("variation_buttons", text)
                self.assertNotIn("[data-variation-button]", text)
