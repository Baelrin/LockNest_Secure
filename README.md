# LockNest_Secure

LockNest_Secure is a secure and user-friendly password manager designed to simplify the management of multiple complex passwords. Built with Python, it leverages the power of encryption to ensure that your passwords are stored safely.

## Features

- **Secure Encryption**: Utilizes the cryptography library to encrypt passwords, ensuring they are stored securely.
- **Environment Variable Support**: Allows for customization of key and password file paths through environment variables.
- **Simple Interface**: Offers a straightforward command-line interface for adding and viewing passwords.
- **Error Handling**: Provides clear error messages and logs for troubleshooting and security purposes.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Baelrin/LockNest_Secure.git
   ```

2. Navigate to the project directory:

   ```bash
   cd LockNest_Secure
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Generate a new encryption key (if necessary):

   ```bash
   python master.py --generate-key
   ```

## Usage

To start using LockNest_Secure, simply run the `master.py` script. You will be prompted to choose between adding a new password or viewing existing ones.

- To add a new password, enter `add` when prompted. You will be asked to enter the account name and password.
- To view existing passwords, enter `view`. The decrypted usernames and passwords will be displayed.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
