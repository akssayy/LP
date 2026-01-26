
f = open("test.txt", "w")
f.write("1, Akshay\n")
f.write("2, Rahul")
f.close()

f = open("test.txt", "r")
content = f.read()
print(content)