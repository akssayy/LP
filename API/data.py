import requests

data = [{"name": "akshay"}]

r = requests.post("http://127.0.0.1:5000/students",
                  json=data)

print(r.json())