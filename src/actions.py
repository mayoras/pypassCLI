from db_connection import mydb
from helpers.crypto import encrypt, decrypt
from helpers.isEmailOrUsername import isEmail
from helpers.verify_user import verify_user
from helpers.copyToClipboard import copy_to_clipboard
import keys


def display_data(header, data):
    print("\n{}".format(header))
    print("Password: ", data[0])
    print("Username: ", data[1])
    print("Email: ", data[2])
    print("Url: ", data[3])
    print("Website: ", data[4], "\n")


def add_new_pwd(args, secret):

    master = verify_user(secret)

    # Get the data
    password = input('Please type the new password: ')
    username = input(
        'Please provide a username for this password (optional): ')
    email = input('Please provide a email: ')
    url = input('Please type the website domain: ')
    website = input('Please type the website name: ')

    # Encrypt the password
    encrypted = encrypt(password, master)

    # Store the data in DB
    cursor = mydb.cursor()
    sql = 'INSERT INTO accounts (password, username, email, url, website) VALUES (%s, %s, %s, %s, %s)'
    val = (encrypted, username, email, url, website)
    cursor.execute(sql, val)

    mydb.commit()

    # Retrieve the new record
    data = get_data(email, website)

    # Display data & copy to clipboard
    display_data("Password added 🔏", data)
    copy_to_clipboard(password)
    exit(0)


def get_password(args, secret):

    master = verify_user(secret)

    # Ask user for email/username and website name
    while True:
        inp = input("Email/Username & website: ")
        inp = inp.split(' ')
        if len(inp) == 2:
            break
        print('Usage: <email/username> <website name>')
        print('Try again please\n')

    emailOrUsername = inp[0]
    website = inp[1]

    # Get data from database, one password should return
    data = get_data(emailOrUsername, website)
    if not data:
        print('There\'s no password for this user and website')
        exit(1)
    data = list(data)

    # Decrypt the password
    decrypted = decrypt(data[0], master)
    data[0] = decrypted

    # Update password encryption
    cursor = mydb.cursor()
    new_encrypted = encrypt(decrypted, master)
    sql = 'UPDATE accounts SET password = %s WHERE email = %s AND website = %s'
    val = (new_encrypted, data[2], data[4])
    cursor.execute(sql, val)

    mydb.commit()

    # Return to user
    display_data('Your password 🔐', data)
    copy_to_clipboard(data[0])
    exit(0)


def get_data(emailOrUsername, website):

    # Check if email or username
    email_or_username = 'username'
    if isEmail(emailOrUsername):
        email_or_username = 'email'

    # Get data from db
    cursor = mydb.cursor()
    sql = 'SELECT * FROM accounts WHERE {} = %s AND website = %s'.format(
        email_or_username)
    val = (emailOrUsername, website)
    cursor.execute(sql, val)
    data = cursor.fetchone()

    return data
