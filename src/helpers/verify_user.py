from src.secret import verify_secret


def verify_user(secret):
    # Verify user
    for c in range(2):
        in_master = input('Please type your master password 🔑\n: ')
        if not verify_secret(in_master, secret):
            print('Incorrect master password ❌\nTry again\n')
            continue

        print('You are in ✅')
        return in_master

    print('Failed two attempts')
    exit(1)
