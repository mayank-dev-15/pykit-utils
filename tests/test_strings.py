"""Tests for pykit.strings"""
import unittest
from pykit.strings import slugify, truncate, camel_to_snake, snake_to_camel, strip_html, count_words, random_string

class TestStrings(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
        self.assertEqual(slugify("  Python 3.12!  "), "python-312")

    def test_truncate(self):
        self.assertEqual(truncate("Hello World", 8), "Hello...")
        self.assertEqual(truncate("Hi", 10), "Hi")

    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("MyClassName"), "my_class_name")

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")

    def test_strip_html(self):
        self.assertEqual(strip_html("<p>Hello</p>"), "Hello")
        self.assertEqual(strip_html("<b>Bold</b> text"), "Bold text")

    def test_count_words(self):
        self.assertEqual(count_words("Hello World"), 2)
        self.assertEqual(count_words(""), 0)

    def test_random_string(self):
        self.assertEqual(len(random_string(10)), 10)
        self.assertNotEqual(random_string(), random_string())

if __name__ == "__main__":
    unittest.main()
