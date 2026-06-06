"""CLI interface for PyKit utilities"""
import argparse, sys
from pykit import __version__

def main():
    parser = argparse.ArgumentParser(description="PyKit CLI - Python Utility Library")
    parser.add_argument('--version', action='version', version=f'PyKit v{__version__}')
    sub = parser.add_subparsers(dest='command')

    p_slug = sub.add_parser('slugify', help='Convert text to slug')
    p_slug.add_argument('text', help='Text to convert')

    p_hash = sub.add_parser('hash', help='Hash a string')
    p_hash.add_argument('text', help='Text to hash')
    p_hash.add_argument('-a', '--algorithm', default='sha256', help='Hash algorithm')

    p_val = sub.add_parser('validate', help='Validate input')
    p_val.add_argument('type', choices=['email', 'url', 'ip', 'json'])
    p_val.add_argument('text', help='Text to validate')

    sub.add_parser('token', help='Generate secure random token')
    sub.add_parser('ip', help='Get public IP address')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    if args.command == 'slugify':
        from pykit.strings import slugify
        print(slugify(args.text))
    elif args.command == 'hash':
        from pykit.crypto import hash_string
        print(hash_string(args.text, args.algorithm))
    elif args.command == 'validate':
        from pykit.validators import is_email, is_url, is_ip, is_json
        validators = {'email': is_email, 'url': is_url, 'ip': is_ip, 'json': is_json}
        result = validators[args.type](args.text)
        print('Valid' if result else 'Invalid')
    elif args.command == 'token':
        from pykit.crypto import generate_token
        print(generate_token())
    elif args.command == 'ip':
        from pykit.network import get_public_ip
        print(get_public_ip())

if __name__ == '__main__':
    main()
