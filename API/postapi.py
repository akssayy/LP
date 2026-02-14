from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "server running"

@app.route("/add", methods=["post"])
def add():
    data = request.json
    name = data["name"]
    age = data["age"]

    return jsonify({
        "message": "user received",
        "name": name,
        "age": age
    })

app.run()