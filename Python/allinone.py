users = []

def show_menu():
    print("\n--- USER SYSTEM ---")
    print("1. Add user")
    print("2. View users")
    print("3. Search user")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add user selected")

    elif choice == "2":
        print("View users selected")

    elif choice == "3":
        print("Search user selected")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
