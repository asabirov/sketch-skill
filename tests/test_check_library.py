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
    def test_hash_name_normalizes_case_and_space(self):
        module = load_module()
        self.assertEqual(module.hash_name("  Sample   Name "), module.hash_name("sample name"))

    def test_check_tree_rejects_a_source_line(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("Source: example\n", encoding="utf-8")
            findings = module.check_tree(pathlib.Path(directory), set())
        self.assertTrue(findings)

    def test_check_tree_rejects_a_hashed_name(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("Sample Name\n", encoding="utf-8")
            hashes = {module.hash_name("sample name")}
            findings = module.check_tree(pathlib.Path(directory), hashes)
        self.assertTrue(findings)

    def test_check_tree_allows_neutral_text(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("A neutral record.\n", encoding="utf-8")
            findings = module.check_tree(pathlib.Path(directory), set())
        self.assertEqual([], findings)

    def test_check_tree_ignores_binary_files(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "frame.png"
            path.write_bytes(b"\x89PNG\r\n\x1a\n\xff")
            findings = module.check_tree(pathlib.Path(directory), set())
        self.assertEqual([], findings)
