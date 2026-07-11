import json
import os

storage_file = "passwords.json"

def load_passwords():
    """Loads all saved passwords from the JSON file.
    Returns an empty dictionary if file doesn't
    exist or is empty.
    """
    if not os.path.exists(storage_file):
        return {}  # return empty dict if file doesn't exist yet

    if os.path.getsize(storage_file)==0:
        return{}
   
    with open(storage_file, "r") as f:
        return json.load(f)
    
def save_passwords(passwords):
    """Saves the passwords dictionary to the JSON file.
    Uses indent=4 for clean readable formatting.
    """
    with open(storage_file,"w") as f:
        json.dump(passwords, f,indent=4)
    print("passwords saved!")