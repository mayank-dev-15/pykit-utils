"""Validation utility functions"""
import re, json

def is_email(text):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, text))

def is_url(text):
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, text, re.IGNORECASE))

def is_ip(text):
    parts = text.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(p) <= 255 for p in parts)
    except ValueError:
        return False

def is_json(text):
    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, TypeError):
        return False
