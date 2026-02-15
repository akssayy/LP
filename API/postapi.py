from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "server running"

@app.route("/student", methods=["post"])
def add_student():
    data = request.json

    name = data["name"]
    course = data["course"]

    return jsonify({
        "message": "student received",
        "name": name,
        "course": course
    })

app.run()