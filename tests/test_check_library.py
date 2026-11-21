import importlib.util
import pathlib
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).parents[1] / "scripts" / "check_library.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_library", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LibraryCheckTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def findings_for(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text(text, encoding="utf-8")
            return self.module.check_file(path)

    def assert_finds_source(self, text):
        findings = self.findings_for(text)
        self.assertTrue(any("Source line" in finding for finding in findings))

    def test_rejects_a_plain_source_note(self):
        self.assert_finds_source("A note source: first")

    def test_rejects_a_source_note_in_an_html_comment(self):
        self.assert_finds_source("<!-- Source: example -->")

    def test_rejects_a_source_note_in_single_star_emphasis(self):
        self.assert_finds_source("*Source:*")

    def test_rejects_a_source_note_in_double_star_emphasis(self):
        self.assert_finds_source("**Source**:")

    def test_rejects_a_source_note_in_underscore_emphasis(self):
        self.assert_finds_source("_Source_:")

    def test_rejects_a_source_note_in_html_tags(self):
        self.assert_finds_source("<b>Source</b>:")

    def test_rejects_a_source_note_in_any_case(self):
        self.assert_finds_source("sOuRcE: example")

    def test_rejects_a_source_note_with_spaces_before_the_colon(self):
        self.assert_finds_source("Source : example")

    def test_allows_neutral_text(self):
        self.assertEqual([], self.findings_for("resource: a list"))
        self.assertEqual([], self.findings_for("the source of the data"))

    def test_rejects_invalid_encoding(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_bytes(b"Source: example\n\xff")
            findings = self.module.check_tree(pathlib.Path(directory))
        self.assertTrue(findings)

    def test_main_checks_a_given_root(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("Source: example\n", encoding="utf-8")
            result = self.module.main(["--root", directory])
        self.assertEqual(1, result)
