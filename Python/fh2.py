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
            
print(users)

for user in users:
    print("user id:", user["id"])
    print("user name:", user["name"])
    print("-----")