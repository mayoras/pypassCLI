import base64
from Crypto.Cipher import AES
import hashlib
import os

def encrypt(pwd, key):
	# Config the cipher
	# private_key = hashlib.sha256(key.encode('utf-8')).digest()
	salt = os.urandom(16)
	private_key = hashlib.pbkdf2_hmac('sha256', key.encode('utf-8'), salt, 100000)
	cipher = AES.new(private_key, AES.MODE_GCM)

	# Cipher the message
	cipher_text, tag = cipher.encrypt_and_digest(pwd.encode('utf-8'))

	cipher_text = base64.b64encode(cipher_text).decode('utf-8')
	tag = base64.b64encode(tag).decode('utf-8')
	nonce = base64.b64encode(cipher.nonce).decode('utf-8')
	salt = base64.b64encode(salt).decode('utf-8')

	return cipher_text + '*' + tag + '*' + nonce + '*' + salt

def decrypt(enc, key):
	try:
		# Get the data
		data = enc.split('*')
		cipher_text = data[0]
		tag = data[1]
		nonce = data[2]
		salt = data[3]

		# Decode from base64
		cipher_text = base64.b64decode(cipher_text)
		tag = base64.b64decode(tag)
		nonce = base64.b64decode(nonce)
		salt = base64.b64decode(salt)

		# Config the cipher
		# private_key = hashlib.sha256(key.encode('utf-8')).digest()
		private_key = hashlib.pbkdf2_hmac('sha256', key.encode('utf-8'), salt, 100000)
		cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

		# Decrypt the message
		decrypted_bin = cipher.decrypt_and_verify(cipher_text, tag)
	except:
		return False
	return decrypted_bin.decode('UTF-8')