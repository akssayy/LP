import request

data = {
    "name": Akshay,
    "age": 20
}

r = response.post("http://127.0.0.1:5000/students", json=data)

print(r.json())