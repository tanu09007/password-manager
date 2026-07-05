from crypto import load_key, encrypt_password, decrypt_password
from storage import load_passwords, save_passwords

class PasswordManager:
    def __init__(self):
       self.key = load_key()
       self.passwords= load_passwords()

    def add_password(self,site,username,password):
        encrypted = encrypt_password(password, self.key)
        self.passwords[site]={
            "username":username,
            "password":encrypted
        }
        save_passwords(self.passwords)
        print(f" Password for '{site}' saved!")
 
    def get_password(self,site):
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
        if self.passwords:
            print("saved sites:")
            for site in self.passwords:
                print(f"  -{site}")
        else:
            print("NO passwords saved yet .")
    
    def delete_password(self,site):
        if site in self.passwords:
            del self.passwords[site]
            save_passwords(self.passwords)
            print(f"password for  {site} deleted successfully!")
        else:
            print (f" password for  '{site}' not found.")    