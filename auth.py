import hashlib
import os

MASTER_PASSWORD_FILE = "master.hash"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup_master_password():
    """First time setup — create master password"""
    print("🔐 Set up your master password")
    password = input("Enter master password: ")
    confirm = input("Confirm master password: ")

    if password != confirm:
        print("❌ Passwords don't match! Try again.")
        return setup_master_password()

    hashed = hash_password(password)
    with open(MASTER_PASSWORD_FILE, "w") as f:
        f.write(hashed)
    print("✅ Master password set!")

def verify_master_password():
    """Check if entered password matches saved hash"""
    password = input("🔑 Enter master password: ")
    hashed = hash_password(password)

    with open(MASTER_PASSWORD_FILE, "r") as f:
        saved_hash = f.read()

    if hashed == saved_hash:
        print("✅ Access granted!")
        return True
    else:
        print("❌ Wrong password! Access denied.")
        return False

def check_master_password_exists():
    """Check if master password is already set"""
    return os.path.exists(MASTER_PASSWORD_FILE)