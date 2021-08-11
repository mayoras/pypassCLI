from src.secret import get_secret
import src.actions as actions
import argparse


def main():
    # Get the secret to verify authenticity
    secret = get_secret()

    # Instance the parser
    parser = argparse.ArgumentParser(
        prog='pypass', description='Unique-user password manager CLI')

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
