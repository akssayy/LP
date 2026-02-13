from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/student")

def student():
    data = ({
        "name": "Akshay","course": "Full Stack","level": "learner"},
        {"name": "Sam", "course": "Java"},
        {"name": "Ab Devillers", "course": "Bullying MI"})
    return jsonify(data)
app.run()