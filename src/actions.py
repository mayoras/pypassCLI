from src.db_connection import mydb
from src.helpers.crypto import encrypt, decrypt
from src.helpers.verify_user import verify_user
from src.helpers.copyToClipboard import copy_to_clipboard
from src.helpers.random import gen_random_str
from src.secret import change_secret
from src.lib.input import get_db_keys, get_new_pwd
from src.lib.db import get_data, remove_data, update_pwd

def display_data(header, data):
	print("\n{}\n".format(header))
	print("Password: ", data[0])
	print("Username: ", data[1])
	print("Email: ", data[2])
	print("Url: ", data[3])
	print("Website: ", data[4], "\n")


def decrypt_data(data, master):
	data = list(data)

	# Decrypt the password
	decrypted = decrypt(data[0], master)
	data[0] = decrypted

	update_pwd(data, master)

	return data

#############################
########## ACTIONS ##########
#############################

def add_new_pwd(args, secret):

	master = verify_user(secret)

	# Get the data
	if args.random:
		size = int(args.size) if args.size else 10
		password = gen_random_str(size)
	else:
		password = input("Please type the new password: ")

	username = input("Please provide a username for this password (optional): ")
	email = input("Please provide a email: ")
	url = input("Please type the website domain: ")
	website = input("Please type the website name: ")

	# Encrypt the password
	encrypted = encrypt(password, master)

	# Store the data in DB
	cursor = mydb.cursor()
	sql = "INSERT INTO accounts (password, username, email, url, website) VALUES (%s, %s, %s, %s, %s)"
	val = (encrypted, username, email, url, website)
	cursor.execute(sql, val)

	mydb.commit()

	# Retrieve the new record
	data = get_data(email, website)

	# Display data & copy to clipboard
	display_data("Password added 🔏: {}".format(password), data)
	copy_to_clipboard(password)
	return


def get_password(args, secret):

	master = verify_user(secret)

	if args.all:

		### GET ALL PASSWORDS ###

		data = get_data()
		if not data:
			print("There are no passwords")
			print("Add one with: pypass.py add")
			exit(0)
		for d in data:
			d = decrypt_data(d, master)
			display_data("👤 User: {}, 🌐website URL: {}".format(d[1], d[3]), d)
		return

	### GET PASSWORD BY EMAIL/USERNAME & WEBSITE NAME ###
	emailOrUsername, website = get_db_keys()

	# Get data from database, one password should return
	data = get_data(emailOrUsername, website)
	if not data:
		print("There's no password for this user and website.")
		exit(1)

	data = decrypt_data(data, master)

	# Return to user
	display_data("Your password 🔐", data)
	copy_to_clipboard(data[0])
	return


def rm_password(args, secret):

	master = verify_user(secret)

	emailOrUsername, website = get_db_keys()

	data = get_data(emailOrUsername, website)

	confirm = input('Are you sure? [y(es), n(o)] ')
	if confirm == 'y' or confirm == 'yes':
		if remove_data(emailOrUsername, website):
			display_data("Password removed 🚮", data)
		else:
			print("Password could not be deleted.")
			exit(1)
	elif confirm == 'n' or confirm == 'no':
		print('Password was not removed.')
	else:
		print('Option {} is not valid'.format(confirm))
		exit(1)

	return

def change_pwd(args, secret):

	if not (args.master or args.password):
		print('Usage: pypass change <-p | -m>')
		exit(1)

	master = verify_user(secret)

	if args.master:

		if args.random or args.size:
			print('Master key cannot be random')
			exit(1)

		## Change master key

		new_master = get_new_pwd()

		change_secret(new_master)

		# Updates the password with new master key
		data = get_data()
		if not data:
			return

		for d in data:
			decrypted_data = decrypt_data(d, master)
			update_pwd(decrypted_data, new_master)
		print('✨ Master key changed successfully')

	elif args.password:

		# Get the keys to change the password
		emailOrUsername, website = get_db_keys()

		# emailOrUsername = inp[0]
		# website = inp[1]

		data = get_data(emailOrUsername, website)
		data = list(data)

		new_pwd = get_new_pwd(args=args)
		if new_pwd:
			data[0] = new_pwd
			update_pwd(data, master)
			display_data("Password changed:", data)
		else:
			return
		return
