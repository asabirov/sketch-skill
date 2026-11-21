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

    def test_hash_name_matches_a_literal_digest(self):
        module = load_module()
        self.assertEqual(
            "72b88afc6d5b2c5b0f7fd0432702341d7dc73189f9e2b93d3faf931927e1725a",
            module.hash_name("sample name"),
        )

    def test_check_tree_rejects_a_source_line(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("Source: example\n", encoding="utf-8")
            findings = module.check_tree(pathlib.Path(directory), set())
        self.assertTrue(findings)

    def test_check_tree_rejects_a_source_inside_an_html_comment(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("<!-- Source: example -->\n", encoding="utf-8")
            findings = module.check_tree(pathlib.Path(directory), set())
        self.assertTrue(findings)

    def test_check_tree_rejects_a_second_midline_source_line(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("A note source: first\nA note source: second\n", encoding="utf-8")
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
            findings = module.check_tree(pathlib.Path(directory), {module.hash_name("sample name")})
        self.assertEqual([], findings)

    def test_check_tree_rejects_invalid_encoding(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_bytes(b"Source: example\n\xff")
            findings = module.check_tree(pathlib.Path(directory), set())
        self.assertTrue(findings)

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

    def test_main_checks_a_given_root(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "pattern.md"
            path.write_text("Source: example\n", encoding="utf-8")
            result = module.main(["--root", directory])
        self.assertEqual(1, result)
