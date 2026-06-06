"""Network utility functions"""
import socket, urllib.request

def get_public_ip():
    try:
        return urllib.request.urlopen('https://api.ipify.org', timeout=5).read().decode()
    except:
        return "Unknown"

def is_port_open(host, port, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def check_url(url, timeout=10):
    try:
        req = urllib.request.Request(url, method='HEAD')
        resp = urllib.request.urlopen(req, timeout=timeout)
        return resp.status < 400
    except:
        return False
