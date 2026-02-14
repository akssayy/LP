from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/a")
def first():
    return "first"

@app.route("/b")
def second():
    return "Second"

app.run()