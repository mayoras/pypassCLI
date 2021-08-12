from src.helpers.random import gen_random_str

def get_new_pwd(args=None):

	if args and args.random:
		size = int(args.size) if args.size else 20
		new_pwd = gen_random_str(size)
	else:
		while True:
				new_pwd = input('Type new password: ')
				if new_pwd == input('Confirm new password: ') or len(new_pwd) < 1:
					break
				print('FAIL: new password confirmation failed\nTry Again\n')

	# Confirm
	print('Your new password is:', new_pwd)
	confirm = input('Are you sure you want to make changes? [y(es) n(o)]: ').lower()
	if confirm == 'n' or confirm == 'no':
		print('\nPassword has no created or change')
		return
	elif confirm != 'y' and confirm != 'yes':
		print('Option is not valid')
		exit(1)
	return new_pwd

def get_db_keys():
		while True:
			inp = input("Password\'s email/username & website: ")
			inp = inp.split(" ")
			if len(inp) == 2:
				break
			print("Usage: <email/username> <website name>")
			print("Try again please\n")

		emailOrUsername = inp[0]
		website = inp[1]
		return emailOrUsername, website