from flask import Flask, jsonify

app = Flask(__name__)

users = []

@app.route("/multipy/<int:num1>/<int:num2>")
def multipy(num1, num2):
    return jsonify({"sum": num1 * num2})

app.run()