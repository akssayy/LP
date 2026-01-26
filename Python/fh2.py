import os

users = []

if os.path.exists("test.txt"):
    with open("test.txt", "r") as f:
        for line in f: 
            line = line.strip()
            parts = line.split(",")

            user = {
                "id": parts[0],
                "name": parts[1].strip()
            }

            users.append(user)
            
"""print(users)"""

for user in users:
    print(f"Id: {user['id']} | Name: {user['name']}")


print("Total users: ", len(users))


search_id = input("enter a id to search: ")

found = False

for user in users:
    if search_id == user["id"]:
        print(f"user found: ", {user["name"]})
        found = True
        break

if not found:
    print("User not found")
