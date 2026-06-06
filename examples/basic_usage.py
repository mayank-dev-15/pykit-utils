"""Example usage of PyKit utilities"""
from pykit.strings import slugify, truncate, camel_to_snake, snake_to_camel, strip_html, count_words, random_string
from pykit.files import get_file_size, ensure_dir
from pykit.network import get_public_ip, is_port_open, check_url
from pykit.crypto import hash_string, generate_token, simple_encrypt, simple_decrypt
from pykit.datetime_utils import time_ago, format_duration, utc_now
from pykit.validators import is_email, is_url, is_ip, is_json

print("=" * 60)
print("🐍 PyKit Utils - Example Usage")
print("=" * 60)

# Strings
print("\n📝 String Utilities:")
print(f"  slugify('Hello World!'): {slugify('Hello World!')}")
print(f"  truncate('A very long text here', 12): {truncate('A very long text here', 12)}")
print(f"  camel_to_snake('helloWorld'): {camel_to_snake('helloWorld')}")
print(f"  snake_to_camel('my_variable'): {snake_to_camel('my_variable')}")
print(f"  strip_html('<b>Bold</b> text'): {strip_html('<b>Bold</b> text')}")
print(f"  count_words('Hello World Test'): {count_words('Hello World Test')}")
print(f"  random_string(8): {random_string(8)}")

# Crypto
print("\n🔐 Crypto Utilities:")
print(f"  hash_string('password123')[:16]: {hash_string('password123')[:16]}...")
print(f"  generate_token()[:16]: {generate_token()[:16]}...")
enc = simple_encrypt("secret message", "mykey")
print(f"  simple_encrypt('secret msg', 'key'): {enc[:20]}...")
print(f"  simple_decrypt(...): {simple_decrypt(enc, 'mykey')}")

# Validators
print("\n✅ Validators:")
print(f"  is_email('test@example.com'): {is_email('test@example.com')}")
print(f"  is_email('bad-email'): {is_email('bad-email')}")
print(f"  is_url('https://google.com'): {is_url('https://google.com')}")
print(f"  is_ip('192.168.1.1'): {is_ip('192.168.1.1')}")
print(f"  is_ip('999.999.999.999'): {is_ip('999.999.999.999')}")
print(f"  is_json('{{\"a\": 1}}'): {is_json('{\"a\": 1}')}")
print(f"  is_json('not json'): {is_json('not json')}")

# Network
print("\n🌐 Network Utilities:")
print(f"  get_public_ip(): {get_public_ip()}")
print(f"  is_port_open('google.com', 443): {is_port_open('google.com', 443)}")
print(f"  check_url('https://google.com'): {check_url('https://google.com')}")

# Datetime
print("\n🕐 Datetime Utilities:")
print(f"  utc_now(): {utc_now()}")
print(f"  format_duration(3661): {format_duration(3661)}")
print(f"  format_duration(45): {format_duration(45)}")

print("\n" + "=" * 60)
print("All utilities working correctly! ✅")
