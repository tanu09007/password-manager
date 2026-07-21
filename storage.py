import json
import os

STORAGE_FILE = "passwords.json"

def load_passwords():
    """Loads all saved passwords from the JSON file.
    Returns an empty dictionary if file doesn't
    exist or is empty.
    """
    if not os.path.exists(STORAGE_FILE):
        return {}  # return empty dict if file doesn't exist yet

    if os.path.getsize(STORAGE_FILE) == 0:
        return{}
   
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)
    
def save_passwords(passwords):
    """Saves the passwords dictionary to the JSON file.
    Uses indent=4 for clean readable formatting.
    """
    with open(STORAGE_FILE,"w") as f:
        json.dump(passwords, f, indent=4)
    print("passwords saved!")