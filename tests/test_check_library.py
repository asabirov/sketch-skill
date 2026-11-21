import contextlib
import io
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

    def test_hash_name_normalizes_non_alphanumeric_separators(self):
        module = load_module()
        expected = module.hash_name("sample name")
        self.assertEqual(expected, module.hash_name("Sample-name"))
        self.assertEqual(expected, module.hash_name("sample_name"))
        self.assertEqual(expected, module.hash_name("sample'name"))

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

    def test_check_tree_rejects_a_hashed_path_part(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            path = root / "sample-inbox" / "pattern.md"
            path.parent.mkdir()
            path.write_text("A neutral record.\n", encoding="utf-8")
            findings = module.check_tree(root, {module.hash_name("sample")})
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

    def test_hash_ignores_empty_lines(self):
        module = load_module()
        output = io.StringIO()
        original_stdin = module.sys.stdin
        try:
            module.sys.stdin = io.StringIO("\nSample Name\n")
            with contextlib.redirect_stdout(output):
                module.main(["--hash"])
        finally:
            module.sys.stdin = original_stdin
        self.assertEqual(module.hash_name("sample name") + "\n", output.getvalue())
