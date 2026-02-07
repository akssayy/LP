import json

data = {"akshay": 23400}

f = open("data.json", "w")

json.dump(data, f)

f.close()

