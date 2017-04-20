import unittest
import io

from typing import IO

from yamldown import yamldown

def yaml_first_yamldown() -> str:
    lines = [
        "---",
        "things:",
        "  - hello",
        "  - world",
        "foo: bar",
        "---",
        "This is some markdown text"
    ]
    return "\n".join(lines)

def just_yaml() -> str:
    lines = [
        "---",
        "things:",
        "  - hello",
        "  - world",
        "foo: bar"
    ]
    return "\n".join(lines)

def just_md() -> str:
    return "This is some markdown text"

def md_first_yamldown() -> str:
    lines = [
        "This is some markdown text",
        "---",
        "things:",
        "  - hello",
        "  - world",
        "foo: bar",
        "---"
    ]
    return "\n".join(lines)

def buffer_with(contents: str) -> yamldown.Buffer:
    b = yamldown.Buffer()
    b.append(contents)
    return b

def string_document(contents: str) -> IO[str]:
    return io.StringIO(contents)


class TestLoad(unittest.TestCase):

    def test_yaml_start_at_start(self):
        start = yamldown._is_yaml_start("---\n", yamldown.Buffer())
        self.assertTrue(start)

    def test_yaml_not_started(self):
        start = yamldown._is_yaml_start("foo", yamldown.Buffer())
        self.assertFalse(start)

    def test_yaml_already_started(self):
        start = yamldown._is_yaml_start("- foo\n", buffer_with("---\n"))
        self.assertFalse(start)

    def test_yaml_end_at_end(self):
        start = yamldown._is_yaml_end("---\n", buffer_with("---\n- foo\n"))
        self.assertTrue(start)

    def test_yaml_not_ended(self):
        start = yamldown._is_yaml_end("- foo\n", buffer_with("---\n- foo\n"))
        self.assertFalse(start)

    def test_yaml_not_started(self):
        start = yamldown._is_yaml_end("foo", yamldown.Buffer())
        self.assertFalse(start)

    def test_load_yaml_first(self):
        doc = string_document(yaml_first_yamldown())
        yml_contents, md_contents = yamldown._load(doc)

        expected_yml = {
            "things": [
                "hello",
                "world"
            ],
            "foo": "bar"
        }
        expected_md = "This is some markdown text"

        self.assertEqual(yml_contents, expected_yml)
        self.assertEqual(md_contents, expected_md)

    def test_load_md_first(self):
        doc = string_document(md_first_yamldown())
        yml_contents, md_contents = yamldown._load(doc)

        expected_yml = {
            "things": [
                "hello",
                "world"
            ],
            "foo": "bar"
        }
        expected_md = "This is some markdown text"

        self.assertEqual(yml_contents, expected_yml)
        self.assertEqual(md_contents, expected_md)

class TestDump(unittest.TestCase):

    def test_dump_yaml_first(self):
        yml = {
            "things": [
                "hello",
                "world"
            ],
            "foo": "bar"
        }
        md = "This is some markdown text"

        yamldown_dump = yamldown._dump(yml, md)
        docdump = string_document(yamldown_dump)
        expected = string_document(yaml_first_yamldown())

        self.assertEqual(yamldown._load(docdump), yamldown._load(expected))

    def test_dump_md_first(self):
        yml = {
            "things": [
                "hello",
                "world"
            ],
            "foo": "bar"
        }
        md = "This is some markdown text"

        yamldown_dump = yamldown._dump(yml, md, yamlfirst=True)
        docdump = string_document(yamldown_dump)
        expected = string_document(md_first_yamldown())

        self.assertEqual(yamldown._load(docdump), yamldown._load(expected))



if __name__ == "__main__":
    unittest.main()
