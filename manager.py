from crypto import load_key, encrypt_password, decrypt_password
from storage import load_passwords, save_passwords

class PasswordManager:
    """
    Core class that manages all password operations.
    Handles adding, retrieving, listing, and deleting passwords.
    All passwords are encrypted before saving.
    """

    def __init__(self):
       """
    Loads the encryption key and existing passwords
    when the PasswordManager is created.
    """
       self.key = load_key()
       self.passwords= load_passwords()

    def add_password(self,site,username,password):
        """
        Encrypts and saves a new password for a site.
        Overwrites if site already exists.
        """
        encrypted = encrypt_password(password, self.key)
        self.passwords[site]={
            "username":username,
            "password":encrypted
        }
        save_passwords(self.passwords)
        print(f" Password for '{site}' saved!")
 
    def get_password(self,site):
        """
        Retrieves and decrypts the password for a site.
        Returns a dictionary with username and password,
        or None if site is not found.
        """
        if site in self.passwords:
            data = self.passwords[site]
            decrypted = decrypt_password( data["password"],self.key)
            return{
               "username":data["username"],
               "password":decrypted
           } 
        else:
            print(f"No pass found in'{site}'")
            return None
    
    def list_sites(self):
        """
        Prints all saved site names.
        Shows a message if no passwords are saved yet.
        """
        if self.passwords:
            print("saved sites:")
            for site in self.passwords:
                print(f"  -{site}")
        else:
            print("NO passwords saved yet .")
    
    def delete_password(self,site):
        """
        Deletes the password entry for a site.
        Saves updated passwords to file after deletion.
        """
        if site in self.passwords:
            del self.passwords[site]
            save_passwords(self.passwords)
            print(f"password for  {site} deleted successfully!")
        else:
            print (f" password for  '{site}' not found.")    