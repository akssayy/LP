import requests

data = [{"name": "akshay",
        "course": "Python full stack"}]

r = requests.post("http://127.0.0.1:5000/students",
                  json=data)

print(r.json())