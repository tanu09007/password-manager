import json
import os

storage_file = "passwords.json"

def load_passwords():
    """Load passwords from the json file."""
    if not os.path.exists(storage_file):
        return {}  # return empty dict if file doesn't exist yet

    if os.path.getsize(storage_file)==0:
        return{}
   
    with open(storage_file, "r") as f:
        return json.load(f)
    
def save_passwords(passwords):
    """save all pass in json file"""
    with open(storage_file,"w") as f:
        json.dump(passwords, f,indent=4)
    print("passwords saved!")