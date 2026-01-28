"""with open("test.txt", "a") as f:
    f.write("\nnow the file has more content")

with open("test.txt") as f:
    print(f.read())"""

with open("test.txt", "w") as f:
    f.write("i have deleted the content") 

with open("test.txt") as f:
    print(f.read())