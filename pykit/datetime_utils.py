"""Datetime utility functions"""
from datetime import datetime, timezone

def time_ago(dt):
    now = datetime.now(timezone.utc) if dt.tzinfo else datetime.utcnow()
    diff = now - dt
    seconds = int(diff.total_seconds())
    if seconds < 60: return f"{seconds}s ago"
    if seconds < 3600: return f"{seconds//60}m ago"
    if seconds < 86400: return f"{seconds//3600}h ago"
    if seconds < 2592000: return f"{seconds//86400}d ago"
    return f"{seconds//2592000}mo ago"

def format_duration(seconds):
    if seconds < 60: return f"{seconds}s"
    if seconds < 3600: return f"{seconds//60}m {seconds%60}s"
    if seconds < 86400: return f"{seconds//3600}h {(seconds%3600)//60}m"
    return f"{seconds//86400}d {(seconds%86400)//3600}h"

def utc_now():
    return datetime.now(timezone.utc)
