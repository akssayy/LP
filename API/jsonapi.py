from flask import Flask, jsonify

app = Flask(__name__)

students_data = ({
        1:{"name": "Akshay","course": "Full Stack","level": "learner"},
        2:{"name": "Sam", "course": "Java"},
        3:{"name": "Ab Devillers", "course": "Bullying MI"},
        18:{"name": "Virat kholi", "work": "pitah-e-pakistan"}
        })

@app.route("/student/<int:id>")
def get_student(id):
    if id in students_data:
        return jsonify(students_data[id])
    return jsonify({"error": "students not found"})
app.run()