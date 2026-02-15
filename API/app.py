from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "server running"

#Add students
@app.route("/student", methods= ["post"])
def add_student():
    data = request.json

    if not data:
        return jsonify({"error": "no data JSON recived"})
    
    students.append(data)

    return jsonify({
        "message": "student added",
        "total_students": len(students)
    })
#view all students
@app.route("/students")
def get_student():
    return jsonify(students)


app.run()