from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "server is running"

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    students.append(data)

    return jsonify({"message": "student added",
    "students": students})

@app.route("/send", methods=["POST"])
def receive():
    data = request.json
    return jsonify({"you_sent": data
    })

@app.route("/test")
def test():
    return jsonify ({"message": "working"}), 200

app.run(debug=True)

