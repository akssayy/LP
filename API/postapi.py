from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "server running"

@app.route("/student", methods=["post"])
def add_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is requred"}), 400
    
    errors = []
    
    name = data.get("name")
    age = data.get("age")

    if not name:
        errors.append("Name is required")

    el if len(name) > 3:
        errors.append("Name should be greater than 3 chars")
    


    return jsonify({
        "message": "student received",
        "name": name,
        "course": course
    })

app.run()