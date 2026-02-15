import requests

data = {
    "name": "sam",
    "course": "python"
}

r = requests.post("http://127.0.0.1:5000/student",
json=data
)

print(r.json())