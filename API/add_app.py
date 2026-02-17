from flask import Flask, jsonify

app = Flask(__name__)

users = []

@app.route("/power/<int:num1>/<int:num2>")
def power(num1, num2):
    return jsonify({"power": num1 ** num2})

app.run()