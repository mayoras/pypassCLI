import base64
from Crypto.Cipher import AES
import hashlib

def encrypt(pwd, key):
	# Config the cipher
	private_key = hashlib.sha256(key.encode('utf-8')).digest()
	cipher = AES.new(private_key, AES.MODE_GCM)

	# Cipher the message
	cipher_text, tag = cipher.encrypt_and_digest(pwd.encode('utf-8'))

	cipher_text = base64.b64encode(cipher_text).decode('utf-8')
	tag = base64.b64encode(tag).decode('utf-8')
	nonce = base64.b64encode(cipher.nonce).decode('utf-8')

	return cipher_text + '*' + tag + '*' + nonce

def decrypt(enc, key):
	try:
		# Get the data
		data = enc.split('*')
		cipher_text = data[0]
		tag = data[1]
		nonce = data[2]

		# Decode from base64
		cipher_text = base64.b64decode(cipher_text)
		tag = base64.b64decode(tag)
		nonce = base64.b64decode(nonce)

		# Config the cipher
		private_key = hashlib.sha256(key.encode('utf-8')).digest()
		cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

		# Decrypt the message
		decrypted_bin = cipher.decrypt_and_verify(cipher_text, tag)
	except:
		return False
	return decrypted_bin.decode('UTF-8')