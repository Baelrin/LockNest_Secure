import getpass
import logging
import os

from cryptography.fernet import Fernet

logging.basicConfig(filename="app.log", level=logging.INFO)


def write_key():
    """
    Generates a new Fernet key and writes it to a file.
    The file path is determined by the KEY_FILE_PATH environment variable,
    defaulting to key.key if the variable is not set.
    """
    key = Fernet.generate_key()
    with open(os.getenv("KEY_FILE_PATH", "key.key"), "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the Fernet key from a file specified by the KEY_FILE_PATH environment variable,
    falling back to key.key if the variable is not set.

    Raises:
        FileNotFoundError: If the key file does not exist, logging an error and
        suggesting to generate a new key using write_key().

    Returns:
        The loaded key.
    """
    try:
        with open(os.getenv("KEY_FILE_PATH", "key.key"), "rb") as file:
            key = file.read()
        return key
    except FileNotFoundError as e:
        logging.error("Key file not found. Please generate a new key.")
        raise FileNotFoundError(
            "Key file not found. Please generate a new key. Use 'write_key()' function to generate a new key."
        ) from e


def view(fer):
    """
    Displays the decrypted usernames and passwords stored in the file specified by the
    PASSWORDS_FILE_PATH environment variable, defaulting to passwords.txt.

    Args:
        fer (Fernet): An instance of Fernet initialized with the correct key.

    Raises:
        FileNotFoundError: If the passwords file does not exist, records an error in the log.
    """
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
    """
    Adds a new username and encrypted password to the file specified by the
    PASSWORDS_FILE_PATH environment variable, defaulting to passwords.txt.

    Args:
        fer (Fernet): An instance of Fernet initialized with the correct key.

    Raises:
        FileNotFoundError: If the passwords file does not exist, records an error in the log.
    """
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
            print("Invalid mode. Please enter 'view' or 'add'.")
            continue
else:
    print("Key not loaded. Please generate a new key.")
