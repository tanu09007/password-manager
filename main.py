from manager import PasswordManager
from auth import setup_master_password, verify_master_password, check_master_password_exists
from generator import generate_password

def main():
    # Master password check
    if not check_master_password_exists():
        setup_master_password()
    
    if not verify_master_password():
        return  # stop program if wrong password

    pm = PasswordManager()

    while True:
        print("\n🔐 Password Manager")
        print("1. Add password")
        print("2. Get password")
        print("3. List all sites")
        print("4. Delete password")
        print("5. Generate random password")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            site = input("Enter site: ")
            username = input("Enter username: ")
            print("Leave blank to generate a random password")
            password = input("Enter password: ")
            if password == "":
                password = generate_password()
                print(f"🎲 Generated password: {password}")
            pm.add_password(site, username, password)

        elif choice == "2":
            site = input("Enter site: ")
            result = pm.get_password(site)
            if result:
                print(f"\n👤 Username: {result['username']}")
                print(f"🔑 Password: {result['password']}")

        elif choice == "3":
            pm.list_sites()

        elif choice == "4":
            site = input("Enter site: ")
            pm.delete_password(site)

        elif choice == "5":
            length = input("Enter password length (default 12): ")
            length = int(length) if length else 12
            password = generate_password(length)
            print(f"🎲 Generated password: {password}")

        elif choice == "6":
            print("👋 Bye!")
            break

        else:
            print("❌ Invalid choice! Enter 1-6")

main()