# 🐍 PyKit Utils — Python Utility Library

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge)

**A comprehensive Python utility library for strings, files, network, crypto, datetime, and validation.**

`pip install pykit-utils`

</div>

---

## ✨ Features

- 📝 **Strings** — slugify, truncate, camelCase ↔ snake_case, strip HTML, word count, random strings
- 📁 **Files** — read/write JSON, file hashing, find files, ensure directories, human-readable sizes
- 🌐 **Network** — public IP lookup, port checking, URL reachability
- 🔐 **Crypto** — SHA-256/MD5 hashing, secure token generation, simple encrypt/decrypt
- 🕐 **Datetime** — time-ago formatting, duration formatting, UTC now
- ✅ **Validators** — email, URL, IP, JSON validation
- 💻 **CLI** — command-line interface for all utilities

## 🚀 Quick Start

```bash
pip install pykit-utils
```

```python
from pykit.strings import slugify, camel_to_snake
from pykit.validators import is_email, is_url
from pykit.crypto import hash_string, generate_token

# Strings
slugify("Hello World!")        # "hello-world"
camel_to_snake("helloWorld")    # "hello_world"

# Validators
is_email("test@example.com")   # True
is_url("https://google.com")   # True

# Crypto
hash_string("password")        # SHA-256 hex digest
generate_token()               # Secure random hex token
```

## 📖 CLI Usage

```bash
# Slugify text
pykit slugify "Hello World!"

# Hash a string
pykit hash "my password" -a sha256

# Validate
pykit validate email test@example.com
pykit validate url https://google.com
pykit validate ip 192.168.1.1
pykit validate json '{"key": "value"}'

# Generate token
pykit token

# Get public IP
pykit ip
```

## 📁 Project Structure

```
pykit-utils/
├── pykit/
│   ├── __init__.py          # Package init with exports
│   ├── strings.py           # String utilities
│   ├── files.py             # File utilities
│   ├── network.py           # Network utilities
│   ├── crypto.py            # Crypto utilities
│   ├── datetime_utils.py    # Datetime utilities
│   ├── validators.py        # Validation utilities
│   └── cli.py               # CLI interface
├── tests/
│   ├── test_strings.py      # String tests
│   ├── test_validators.py   # Validator tests
│   └── test_crypto.py       # Crypto tests
├── examples/
│   └── basic_usage.py       # Usage examples
├── pyproject.toml           # Package config
└── README.md                # This file
```

## 🧪 Running Tests

```bash
pip install -e .
python -m pytest tests/ -v
```

## 🛠️ Tech Stack

- **Python 3.8+** — Core language
- **setuptools** — Packaging
- **pytest** — Testing
- **argparse** — CLI (stdlib)
- **hashlib / secrets** — Crypto (stdlib)
- **socket / urllib** — Network (stdlib)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ by [Mayank Basena](https://github.com/mayank-dev-15)

</div>

---

## ⚠️ Attribution & Credit Notice

This project is created and maintained by **Mayank Basena** ([@mayank-dev-15](https://github.com/mayank-dev-15)).

If you fork, use, modify, or derive work from this repository, **you must give proper credit** to the original author. This includes:

- Keeping this attribution section intact in any fork or derivative work
- Crediting **Mayank Basena** in your project's README or documentation
- Linking back to the original repository

**Failure to provide proper credit is a violation of the spirit of open source and may result in a DMCA takedown request.**

> *"No AI. No Shortcuts."* — Mayank Basena
