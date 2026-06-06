"""File utility functions"""
import json, hashlib, os, pathlib

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json(filepath, data, indent=2):
    ensure_dir(os.path.dirname(filepath))
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=indent)

def get_file_hash(filepath, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def find_files(directory, pattern='*'):
    return list(pathlib.Path(directory).rglob(pattern))

def ensure_dir(directory):
    if directory:
        os.makedirs(directory, exist_ok=True)

def get_file_size(filepath):
    size = os.path.getsize(filepath)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"
