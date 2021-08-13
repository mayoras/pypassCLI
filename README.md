## PypassCLI
A dead simple password manager CLI written in Python, using MySQL database

# Create database
```bash
mysql -u <user> -p <password> < ./database/db.sql
```

# Install python module
```bash
sudo sh install.sh
```

# Add keys
Open the keys.py file and fill out the proper database credentials.
```python
keys = {
    'user': '<db_username>',
    'password': '<password>',
    'database': 'pypass_db'
}
```

# Usage

## Add command
To add a password, simply put the add command to open a form to create your password
```bash
./pypass.py add
```
To add a random password, use the -r option and -s to specify the length of the password. Default size is 10
```bash
usage: pypass add [-h] [-r] [-s SIZE]
```


## Get command
To get a password, as well as the add command, use get to open a form to get your password.
```bash
./pypass.py get
```
To get all passwords:
```bash
./pypass.py get [-a]
```

## Change command
To change command has two functionalities, change a password or change the master password.

To change the master password
```bash
./pypass.py change -m
```

To change a password:
```bash
./pypass.py change -p [-r] [-s]
```
Use options `-r` and `-s` to specify a random password. The default size is 10

> *Note: You only will be able to change your password, other additional information such like your email, username, will not for now.*

## Remove command
To remove a password, type:
```bash
./pypass.py remove
```
to select what password you would remove.
#
Feel free to share ideas or contribute to this small project.
