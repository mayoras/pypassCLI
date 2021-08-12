from src.helpers.isEmail import isEmail
from src.db_connection import mydb
from src.helpers.crypto import encrypt

def emailOrUsernameCheck(emailOrUsername):
	email_or_username = "username"
	if isEmail(emailOrUsername):
		email_or_username = "email"
	return email_or_username

def get_data(emailOrUsername=None, website=None):

	cursor = mydb.cursor()

	if not (emailOrUsername or website):
		# Get all passwords
		sql = "SELECT * FROM accounts"
		cursor.execute(sql)
		return cursor.fetchall()

	# Check if email or username
	email_or_username = emailOrUsernameCheck(emailOrUsername)

	# Get data from db
	sql = "SELECT * FROM accounts WHERE {} = %s AND website = %s".format(
		email_or_username
	)
	val = (emailOrUsername, website)
	cursor.execute(sql, val)
	data = cursor.fetchone()

	# Check if password exists
	if not data:
		print("There's no password for this user and website.")
		exit(1)

	return data

def remove_data(emailOrUsername, website):
	try:
		cursor = mydb.cursor()
		# Check if email or username
		email_or_username = emailOrUsernameCheck(emailOrUsername)

		# Get data from db
		sql = "DELETE FROM accounts WHERE {} = %s AND website = %s".format(
			email_or_username
		)
		val = (emailOrUsername, website)
		cursor.execute(sql, val)

		mydb.commit()
	except:
		return False

	return True

def update_pwd(dec_data, master):
	
	# Update password encryption, update nonce
	cursor = mydb.cursor()
	new_encrypted = encrypt(dec_data[0], master)
	sql = "UPDATE accounts SET password = %s WHERE email = %s AND website = %s"
	val = (new_encrypted, dec_data[2], dec_data[4])
	cursor.execute(sql, val)

	mydb.commit()
