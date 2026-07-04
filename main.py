from crypto import generate_key ,save_key ,load_key ,encrypt_password ,decrypt_password
import os

#generate and save key(only 1st time)
if not os.path.exists("secret.key"):
    key = generate_key()
    save_key(key)

#load key
key = load_key()
print(f"key loaded:",key)

#TEST encryption
password ="mypassword123"
print(f"\nOriginal password:{password}")

encrypted = encrypt_password(password,key)
print(f"Encrypted :{encrypted})")

decrypted = decrypt_password(encrypted, key)
print(f"Decrypted :{decrypted}")
