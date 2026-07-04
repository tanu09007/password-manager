from cryptography.fernet import Fernet

def generate_key():
    """A new  encryption key is generated """
    return  Fernet.generate_key()

def save_key(key, filename="secret.key"):
    """Saves the key to file"""
    with open(filename, "wb") as key_file:
        key_file.write(key)
    print("key saved to:",filename)
    
def load_key(filename="secret.key"):
    """loads key from file"""
    with open(filename,"rb") as key_file:
        return key_file.read()
def encrypt_password(password,key):
    """Encrypts a plain txt password"""
    f=Fernet(key)
    encrypted=f.encrypt(password.encode())
    return encrypted.decode()

def decrypt_password(encrypted_password,key):
    """Decrypt an encrypted password"""
    f=Fernet(key)
    decrypted = f.decrypt(encrypted_password.encode())
    return decrypted.decode()
