import json

f = open("data.json", "r")

data = json.load(f)

f.close()

print(data)
