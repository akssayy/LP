import os

FILENAME = "test.txt"
users = []

# ---------- LOAD USERS FROM FILE ----------
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")

            user = {
                "id": parts[0],
                "name": parts[1].strip()
            }

            users.append(user)

# ---------- FUNCTIONS ----------
def show_menu():
    print("\n--- USER SYSTEM ---")
    print("1. Add user")
    print("2. View users")
    print("3. Search user")
    print("4. Exit")

def add_user():
    user_id = input("Enter id: ")
    name = input("Enter name: ")

    user = {"id": user_id, "name": name}
    users.append(user)

    with open(FILENAME, "a") as f:
        f.write(f"\n{user_id}, {name}")

    print("User added and saved.")

def view_users():
    if len(users) == 0:
        print("No users found.")
    else:
        for user in users:
            print(f"Id: {user['id']} | Name: {user['name']}")

def search_user():
    search_id = input("Enter id to search: ")
    found = False

    for user in users:
        if user["id"] == search_id:
            print("User found:", user["name"])
            found = True
            break

    if not found:
        print("User not found.")

# ---------- MAIN LOOP ----------
while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        view_users()
    elif choice == "3":
        search_user()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
