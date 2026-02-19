from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route("/students", methods=["POST"])
def post_student():
    data = request.json
    students.append(data)

    if data["name"] == None:
        return "error, Enter name "
    elif data["age"] == None:
        return "error, age is required"
    return jsonify({"message": "recived", "student": students})

app.run()