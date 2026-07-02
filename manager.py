class PasswordManager:
    def __init__(self):
        self.passwords={}
    def add_password(self,site,username,password):
        self.passwords[site]={
            "username":username,
            "password":password
        }
        print(f" Password for '{site}' saved!")
    def get_password(self,site):
        if site in self.passwords:
            return self.passwords[site]
        else:
            print(f"No pass found in'{site}'")
            return None
    def list_sites(self):
        if self.passwords:
            print("saved sites:")
            for site in self.passwords:
                print(f" -{site}")
        else:
            print("NO passwords saved .")
    def delete_password(self,site):
        if site in self.passwords:
            del self.passwords[site]
            print(f"password for {site} deleted successfully!")
        else:
            print (f" password for  '{site}' not found.")    