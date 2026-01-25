users = []

def show_menu():
    print("\n--- USER SYSTEM ---")
    print("1. Add user")
    print("2. View users")
    print("3. Search user")
    print("4. Exit")

def add_user(users):
     user_id = int(input("Enter user id: "))
     name = input("Enter name: ")

     user = {"id": user_id, "name": name}
     users.append(user)

     print("User added successfully.")


def view_users(users):
        if len(users) == 0:
            print("No users found.")
        else:
            print("\nAll users:")
            for user in users:
                print(user["id"], "-", user["name"])

def search_user(users):
    if len(users) == 0:
        print("no user to search.")
        return
    
    search = input("enter user id or name: ")

    found = False

    for user in users:
        if search == str(user["id"]) or search.lower() == user["name"].lower():
            print("user found:", user ["id"], "-", user["name"])
            found = True
            break

    if not found:
        print("user not found.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_user(users)

    elif choice == "2":
        view_users(users)

    elif choice == "3":
        search_user(users)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
