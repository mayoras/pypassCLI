#!/bin/bash

install_dependencies() {
    apt install python3 pip xclip
    pip install pycryptodome pyperclip mysql-connector-python bcrypt
    touch secret.txt
}

@echo "Installing dependencies..."
install_dependencies

# Execution permission
chmod +x ./pypass.py

# Init pypass to create a master key
python3 pypass.py get -a