#!/usr/bin/env python3

from src.secret import get_secret
import src.actions as actions
import argparse


def main():
	# Get the secret hash key to verify authenticity
	secret = get_secret()

	# Instance the parser
	parser = argparse.ArgumentParser(
		prog='pypass', description='Unique-user password manager CLI')

	subparsers = parser.add_subparsers(title='commands')

	## SubParsers ##

	# Adding password
	add_password = subparsers.add_parser(
		'add', help='Add a new password'
	)
	add_password.add_argument(
		'-r', '--random', help='Generate a random password. Default size of 10', action='store_true'
	)
	add_password.add_argument(
		'-s', '--size', help='Select the size of random password.', type=int
	)
	add_password.set_defaults(func=actions.add_new_pwd)

	# Getting password
	get_password = subparsers.add_parser(
		'get', help='Get a password.'
	)
	get_password.add_argument(
		'-a', '--all', help='Get all passwords.', action='store_true'
	)
	get_password.set_defaults(func=actions.get_password)

	# Removing password
	rm_password = subparsers.add_parser(
		'remove', help='Remove a password.'
	)
	rm_password.set_defaults(func=actions.rm_password)

	# Changing password and master
	change_pwd = subparsers.add_parser(
		'change', help='Change a password or master key.'
	)
	group_change = change_pwd.add_mutually_exclusive_group()
	group_change.add_argument(
		'-m', '--master', help='Change master key.', action='store_true'
	)
	group_change.add_argument(
		'-p', '--password', help='Change password.', action='store_true'
	)
	change_pwd.add_argument(
		'-r', '--random', help='Change to random password. Default size of 10', action='store_true'
	)
	change_pwd.add_argument(
		'-s', '--size', help='Size of random password.', type=int
	)
	change_pwd.set_defaults(func=actions.change_pwd)

	args = parser.parse_args()
	args.func(args, secret)


if __name__ == "__main__":
	main()
