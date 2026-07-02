from manager import PasswordManager

pm =PasswordManager()

pm.add_password("gmail.com","tan1435@gmail.com","pass123")
pm.add_password("git.com","tanu","pass45667")
pm.list_sites()
print (pm.get_password("gmail.com"))
print(pm.get_password("git.com"))
pm.delete_password("git.com")

pm.list_sites()