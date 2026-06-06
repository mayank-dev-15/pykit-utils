"""Tests for pykit.validators"""
import unittest
from pykit.validators import is_email, is_url, is_ip, is_json

class TestValidators(unittest.TestCase):
    def test_is_email(self):
        self.assertTrue(is_email("test@example.com"))
        self.assertTrue(is_email("user.name+tag@domain.co.uk"))
        self.assertFalse(is_email("not-an-email"))
        self.assertFalse(is_email("@nodomain.com"))
        self.assertFalse(is_email(""))

    def test_is_url(self):
        self.assertTrue(is_url("https://example.com"))
        self.assertTrue(is_url("http://localhost:8080/path"))
        self.assertFalse(is_url("not a url"))
        self.assertFalse(is_url("ftp://invalid.com"))

    def test_is_ip(self):
        self.assertTrue(is_ip("192.168.1.1"))
        self.assertTrue(is_ip("10.0.0.1"))
        self.assertTrue(is_ip("255.255.255.255"))
        self.assertFalse(is_ip("256.1.1.1"))
        self.assertFalse(is_ip("not.an.ip"))
        self.assertFalse(is_ip("1.2.3"))

    def test_is_json(self):
        self.assertTrue(is_json('{"key": "value"}'))
        self.assertTrue(is_json('[1, 2, 3]'))
        self.assertTrue(is_json('true'))
        self.assertFalse(is_json('not json'))
        self.assertFalse(is_json('{invalid}'))

if __name__ == "__main__":
    unittest.main()
