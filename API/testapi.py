from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Akshay"},
    {"id": 2, "name": "Sam"}
]

@app.route("/")
def home():
    return "API running"

@app.route("/users")
def get_users():
    return jsonify(users)

app.run()