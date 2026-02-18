from flask import Flask, jsonify

app = Flask(__name__)

users = []

@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    if b == 0:
        return {"error": "cannot divide bY xero"}
    else:
        return jsonify({"divide": a / b})

app.run()