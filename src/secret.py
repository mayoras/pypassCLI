import bcrypt


def get_secret():
    with open('secret.txt', 'r+') as f:
        secret = f.read()
        if not secret:
            pwd = input('Create your master key: ')
            salt = bcrypt.gensalt(10)
            secret = bcrypt.hashpw(pwd.encode('utf-8'), salt)
            secret = secret.decode('utf-8')
            f.write(secret)

    f.close()
    return secret


def verify_secret(pwd, secret):
    if bcrypt.checkpw(pwd.encode('utf-8'), secret.encode('utf-8')):
        return True
    else:
        return False

def change_secret(new_master):
    with open('secret.txt', 'w') as f:
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(new_master.encode('utf-8'), salt)
        hashed = hashed.decode('utf-8')
        f.write(hashed)
    f.close()
    