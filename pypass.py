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
	add_password.add_argument(
		'-r', '--random', help='Generate a random password. Default size of 10', action='store_true'
	)
	add_password.add_argument(
		'-s', '--size', help='Select the size of random password.'
	)
	add_password.set_defaults(func=actions.add_new_pwd)

	get_password = subparsers.add_parser(
		'get', help='Get a password'
	)
	get_password.add_argument(
		'-a', '--all', help='Get all passwords', action='store_true'
	)
	get_password.set_defaults(func=actions.get_password)

	rm_password = subparsers.add_parser(
		'remove', help='Remove a password'
	)
	rm_password.set_defaults(func=actions.rm_password)

	args = parser.parse_args()
	args.func(args, secret)


if __name__ == "__main__":
	main()
