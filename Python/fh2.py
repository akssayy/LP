import os

if os.path.exists("test.txt"):
    with open("test.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            
            print(parts)