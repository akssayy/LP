user_id = input("enter a id: ")
name = input("enter a name: ")

with open("test.txt", "a") as f:
    f.write(f"\n{user_id}, {name}")


print("user saved to file")