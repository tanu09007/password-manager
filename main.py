from manager import PasswordManager

def main():
  pm = PasswordManager()
  
  while True:
    print("\n Password manager")
    print("\n1.Add password")
    print("\n2.Get password")
    print("\n3.List all sites")
    print("\n4.Delete password")
    print("\n5.Exit") 

    choice = input("\nEnter choice:")

    if choice == "1":
      site = input("enter site:")
      username = input("Enter username: ")
      password = input("enter password: ")
      pm.add_password(site,username,password)

    elif choice == "2":
      
      site = input("Enter site: ")
      result = pm.get_password(site)
      if result:
        print(f"\nusername:{result['username']}")
        print(f"password:{result['password']}")

    elif choice == "3":
      pm.list_sites()

    elif choice == "4":
      site = input("enter site:")
      pm.delete_password(site)

    elif choice == "5":
      print("👋 Bye!")
      break

    else:
      print("Invalid choice! Enter 1-5 ")

main()
       