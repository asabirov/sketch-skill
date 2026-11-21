import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).parents[1]
TEMPLATES = ROOT / "templates"


class TemplateListTests(unittest.TestCase):
    def test_gallery_lists_every_template(self):
        gallery = (ROOT / "assets" / "sketch-pages.html").read_text(encoding="utf-8")
        for page in sorted(TEMPLATES.glob("*/*.html")):
            with self.subTest(page=page.name):
                self.assertIn(f"['{page.parent.name}-{page.stem}',", gallery)

    def test_render_orders_every_category(self):
        render = (ROOT / "docs" / "render.py").read_text(encoding="utf-8")
        order = re.findall(r'"([a-z-]+)"', re.search(r"CATEGORY_ORDER = \[(.*?)\]", render, re.S).group(1))
        self.assertEqual(sorted(order), sorted(p.name for p in TEMPLATES.iterdir() if p.is_dir()))


class ChartTemplateTests(unittest.TestCase):
    def test_each_chart_has_a_rule_page(self):
        for page in sorted((TEMPLATES / "chart").glob("*.html")):
            with self.subTest(page=page.name):
                self.assertTrue((ROOT / "references" / "charts" / f"{page.stem}.md").is_file())

    def test_no_chart_scrolls(self):
        for page in sorted((TEMPLATES / "chart").glob("*.html")):
            with self.subTest(page=page.name):
                self.assertNotRegex(page.read_text(encoding="utf-8"), r"overflow(-x)?\s*:\s*(auto|scroll)")


if __name__ == "__main__":
    unittest.main()
