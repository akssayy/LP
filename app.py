from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my first Flask server!"

@app.route("/user")
def user():
    data = {
        "name": "Akshay",
        "role": "student",
        "goal": "full-stack developer"
    }
    return jsonify(data)

app.run()