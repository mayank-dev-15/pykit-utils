"""Cryptographic utility functions"""
import hashlib, secrets, base64

def hash_string(text, algorithm='sha256'):
    return hashlib.new(algorithm, text.encode()).hexdigest()

def generate_token(length=32):
    return secrets.token_hex(length)

def simple_encrypt(text, key):
    key_bytes = key.encode()
    text_bytes = text.encode()
    encrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(text_bytes)])
    return base64.b64encode(encrypted).decode()

def simple_decrypt(encoded_text, key):
    key_bytes = key.encode()
    encrypted = base64.b64decode(encoded_text)
    decrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(encrypted)])
    return decrypted.decode()
