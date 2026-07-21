from cryptography.fernet import Fernet

def generate_key():
    """Generates a new Fernet encryption key.
    Returns the key as bytes.
    """
    return  Fernet.generate_key()

def save_key(key, filename="secret.key"):
    """ Saves the encryption key to a file in binary mode.
    This file must be kept safe — losing it means
    losing access to all saved passwords.
    """
    with open(filename, "wb") as key_file:
        key_file.write(key)
    print("key saved to:",filename)
    
def load_key(filename="secret.key"):
    """Loads the encryption key from file.
    Returns the key as bytes.
    """
    with open(filename,"rb") as key_file:
        return key_file.read()
def encrypt_password(password,key):
    """ Takes a plain text password and encrypts it
    using the Fernet key.
    Returns encrypted password as a string.
    """
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted.decode()

def decrypt_password(encrypted_password,key):
    """Takes an encrypted password and decrypts it
    using the Fernet key.
    Returns the original plain text password.
    """
    f=Fernet(key)
    decrypted = f.decrypt(encrypted_password.encode())
    return decrypted.decode()
