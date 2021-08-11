from secret import get_secret
import actions
from helpers.copyToClipboard import copy_to_clipboard
import argparse


def main():
    # Get the secret to verify authenticity
    secret = get_secret()

    print("-" * 5, "Welcome", "-" * 5)

    # Instance the parser
    parser = argparse.ArgumentParser(
        description='Unique-user password manager CLI')

    subparsers = parser.add_subparsers(title='commands')

    add_password = subparsers.add_parser(
        'add', help='Add a new password'
    )
    add_password.set_defaults(func=actions.add_new_pwd)

    get_password = subparsers.add_parser(
        'get', help='Get a password'
    )
    get_password.set_defaults(func=actions.get_password)

    args = parser.parse_args()
    args.func(args, secret)


if __name__ == "__main__":
    main()
