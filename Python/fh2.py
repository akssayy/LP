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
    print("Id:", user["id"], " | ", end= " " )
    print("Name:", user["name"])
    
search_id = input("enter a id to search: ")
found = False
for user in users:
    if search_id == user["id"]:
        print(f"user found: user{'name'}")
        found = True
        break
    else:
        print("user not found")