import os
import getpass
from cryptography.fernet import Fernet
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)


def write_key():
    key = Fernet.generate_key()
    with open(os.getenv("KEY_FILE_PATH", "key.key"), "wb") as key_file:
        key_file.write(key)


def load_key():
    try:
        with open(os.getenv("KEY_FILE_PATH", "key.key"), "rb") as file:
            key = file.read()
        return key
    except FileNotFoundError:
        logging.error("Key file not found. Please generate a new key.")
        return None


def view():
    try:
        with open(os.getenv("PASSWORDS_FILE_PATH", "passwords.txt"), "r") as f:
            for line in f:
                data = line.rstrip()
                user, passw = data.split("|")
                print(
                    "User:", user, "| Password:", fer.decrypt(passw.encode()).decode()
                )
    except FileNotFoundError:
        logging.error("Passwords file not found.")


def add():
    name = input("Account Name: ")
    pwd = getpass.getpass("Password: ")

    try:
        with open(os.getenv("PASSWORDS_FILE_PATH", "passwords.txt"), "a") as f:
            f.write(f"{name}|{str(fer.encrypt(pwd.encode()).decode())}\n")
    except FileNotFoundError:
        logging.error("Passwords file not found.")


key = load_key()
if key is not None:
    fer = Fernet(key)

    while True:
        mode = input(
            "Would you like to add a new password or view existing ones (view, add), press Q to quit? "
        ).lower()
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue
else:
    print("Key not loaded. Please generate a new key.")
