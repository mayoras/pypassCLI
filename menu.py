from db_connection import mydb
from helpers.encrypt import encrypt, decrypt
import keys
from helpers.isEmailOrUsername import isEmail

def get_main_menu():
	# Main menu

	print('-'*5, 'Select one option', '-'*5)
	print('1. Add new password')
	print('2. Get password')
	print('Q. Exit')

	return input(': ')

def add_new_pwd(key):
	
	# Get the data
	password = input('Please type the new password: ')
	username = input('Please provide a username for this password (optional): ')
	email = input('Please provide a email: ')
	url = input('Please type the website domain: ')
	website = input('Please type the website name: ')

	# Encrypt the password
	password = encrypt(password, key)

	# Store the data in DB
	cursor = mydb.cursor()
	sql = 'INSERT INTO accounts (password, username, email, url, website) VALUES (%s, %s, %s, %s, %s)'
	val = (password, username, email, url, website)
	cursor.execute(sql, val)

	mydb.commit()
	
	# Retrieve the new record
	return get_data(email, website)

def get_password(key):
	# Ask user for email/username and website name
	inp = input("Email/Username & website: ")
	inp = inp.split(' ')

	emailOrUsername = inp[0]
	website = inp[1]

	# Get data from database, one password should return
	data = get_data(emailOrUsername, website)
	if not data:
		return
	data = list(data)

	# Decrypt the password
	decrypted = decrypt(data[0], key)
	data[0] = decrypted

	# Update password encryption
	cursor = mydb.cursor()
	new_encrypted = encrypt(decrypted, key)
	sql = 'UPDATE accounts SET password = %s WHERE email = %s AND website = %s'
	val = (new_encrypted, data[2], data[4])
	cursor.execute(sql, val)

	mydb.commit()

	return data

def get_data(emailOrUsername, website):

	# Check if email or username
	email_or_username = 'username'
	if isEmail(emailOrUsername):
		email_or_username = 'email'

	# Get data from db
	cursor = mydb.cursor()
	sql = 'SELECT * FROM accounts WHERE {} = %s AND website = %s'.format(email_or_username)
	val = (emailOrUsername, website)
	cursor.execute(sql, val)
	data = cursor.fetchone()

	return data
