from manager import PasswordManager

pm = PasswordManager()

# Add a password
pm.add_password("gmail.com","tanu@gmail.com","mypas1234")
pm.add_password("github.com", "tanu09007", "ghpass456")

#list
pm.list_sites()

# Get a password
result = pm.get_password("gmail.com")
if result:
    print(f"\nSite: gmail.com")
    print(f"username:{result['username']}")
    print(f"Password:{result['password']}")

#delete 1
pm.delete_password("github.com")

#list
pm.list_sites