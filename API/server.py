from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "server is running"

@app.route("/greet")
def greet():
    name = request.args.get("name")

    return jsonify({
        "greeting": f"hello {name}"
    })

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

@app.route("/students", methods=["GET"])
def get_student():
    return jsonify(students)

@app.route("/cube/<int:num>")
def square(num):
    return jsonify({
        "number": num,
        "cube": num * num * num
    })

@app.route("/hello")
def hello():
    return jsonify({"msg": "hello"})

@app.route("/test")
def test():
    return jsonify ({"message": "working"}), 200

app.run(debug=True)

