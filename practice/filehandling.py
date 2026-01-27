
f = open("newf.txt", "w")

for i in range(5):
    name = input("enter a name: ")
    f.write(name + "\n")

f.close()
f = open("newf.txt", "r")
content = f.read()
print(content)