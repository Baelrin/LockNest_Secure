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
    except FileNotFoundError as e:
        logging.error("Key file not found. Please generate a new key.")
        raise FileNotFoundError("Key file not found. Please generate a new key.") from e


def view(fer):
    try:
        with open(os.getenv("PASSWORDS_FILE_PATH", "passwords.txt"), "r") as f:
            for line in f:
                data = line.rstrip()
                user, passw = data.split("|")
                print(
                    "User:", user, "| Password:", fer.decrypt(passw.encode()).decode()
                )
    except FileNotFoundError as e:
        logging.error("Passwords file not found.")
        raise FileNotFoundError("Passwords file not found.") from e


def add(fer):
    name = input("Account Name: ")
    pwd = getpass.getpass("Password: ")

    try:
        with open(os.getenv("PASSWORDS_FILE_PATH", "passwords.txt"), "a") as f:
            f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")
    except FileNotFoundError as e:
        logging.error("Passwords file not found.")
        raise FileNotFoundError("Passwords file not found.") from e


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
            view(fer)
        elif mode == "add":
            add(fer)
        else:
            print("Invalid mode.")
            continue
else:
    print("Key not loaded. Please generate a new key.")
