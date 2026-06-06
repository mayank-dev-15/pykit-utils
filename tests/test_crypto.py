"""Tests for pykit.crypto"""
import unittest
from pykit.crypto import hash_string, generate_token, simple_encrypt, simple_decrypt

class TestCrypto(unittest.TestCase):
    def test_hash_string(self):
        self.assertEqual(len(hash_string("test")), 64)  # SHA-256 hex
        self.assertEqual(hash_string("test"), hash_string("test"))
        self.assertNotEqual(hash_string("test1"), hash_string("test2"))

    def test_hash_string_md5(self):
        self.assertEqual(len(hash_string("test", "md5")), 32)

    def test_generate_token(self):
        token = generate_token()
        self.assertEqual(len(token), 64)  # 32 bytes hex
        self.assertNotEqual(generate_token(), generate_token())

    def test_simple_encrypt_decrypt(self):
        key = "mysecretkey"
        original = "Hello, World!"
        encrypted = simple_encrypt(original, key)
        decrypted = simple_decrypt(encrypted, key)
        self.assertEqual(decrypted, original)
        self.assertNotEqual(encrypted, original)

if __name__ == "__main__":
    unittest.main()
