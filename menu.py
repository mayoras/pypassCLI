from db_connection import mydb
from encrypt import encrypt, decrypt
import keys

def get_main_menu():
	# Main menu

	print('-'*5, 'Select one option', '-'*5)
	print('1. Add new password')
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
	return get_password(email, website)

def get_password(email, website):

	# Get data from db
	cursor = mydb.cursor()
	sql = 'SELECT * FROM accounts WHERE email = %s AND website = %s'
	val = (email, website)
	cursor.execute(sql, val)
	data = cursor.fetchone()

	return data
