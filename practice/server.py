from flask import Flask, jsonify, requests

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "server is running"

@app.route("/students", methods="post")
def ger_student():
    return jsonify

app.run()

