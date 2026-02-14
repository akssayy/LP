import requests

data = {
    "name": "AB Devillers",
    "age": 39
}

r = requests.post("http://127.0.0.1:5000/add",
json=data
)

print(r.json())