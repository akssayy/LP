name = input("enter your name: ")
f = open("name.txt", "w")
f.write(name)
f.close

f = open("name.txt", "r")
content = f.read()
print(content)
f.close()