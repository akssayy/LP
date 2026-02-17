from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "server is running"

@app.route("/onlyget")
def onlyget():
    return "get works"

@app.route("/both", methods=["GET", "POST"])
def both():
    return "works for both"

@app.route("/double/<int:num>")
def double(num):
    return {"result": num * 2}

@app.route("/greet/<name>")
def greet(name):
    
    return jsonify({
        "greeting": f"hello {name}"
    })

@app.route("/info/<name>")
def info(name):
    age = request.args.get("age")

    return jsonify({
        "name": name,
        "age": age
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

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return jsonify({"sum": num1 + num2})

@app.route("/students", methods=["GET"])
def get_student():
    return jsonify(students)

@app.route("/cube/<int:num>")
def cube(num):
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

