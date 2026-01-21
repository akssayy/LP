users = []

q = int(input("how many users you want to enter: "))
for i in range(q):
    user_id = int(input("enter a id"))
    user_name = input("enter a name")

    user = {"id": user_id, "name": user_name}
    users.append(user)

print("all users:")
for user in users:
    print(user["id"], "-", user["name"])