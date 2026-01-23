id = input("enter a id : ")
name = input("enter a name: ")

def create_user(id, name):
    create = {"id": id, "name": name}

    return create

result = create_user(id, name)
print(result)