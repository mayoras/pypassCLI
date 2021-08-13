#!/bin/bash

install_dependencies() {
    apt install python3 pip xclip
    pip install pycryptodome pyperclip mysql-connector-python
    touch secret.txt
}

install_CLI() {
    
}

@echo "Installing dependencies..."
install_dependencies
@echo "Installing CLI..."
install_CLI


