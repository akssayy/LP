with open("test.txt", "a") as f:
    f.write("\nnow the file has more content")

with open("test.txt") as f:
    print(f.read())