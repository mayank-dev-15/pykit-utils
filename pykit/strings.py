"""String utility functions"""
import re, random, string

def slugify(text, separator="-"):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', separator, text)
    return text.strip(separator)

def truncate(text, length=100, suffix="..."):
    if len(text) <= length:
        return text
    return text[:length - len(suffix)].rstrip() + suffix

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_camel(name):
    parts = name.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def strip_html(text):
    return re.sub(r'<[^>]+>', '', text)

def count_words(text):
    return len(text.split())

def random_string(length=16, charset=None):
    if charset is None:
        charset = string.ascii_letters + string.digits
    return ''.join(random.choices(charset, k=length))
