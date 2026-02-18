from flask import Flask, jsonify

app = Flask(__name__)

users = []

@app.route("/power/<base>/<exp>")
def power(base, exp):
    base = int(base)
    exp = int(exp)
    if exp < 0 :
        return jsonify({"error": "exp cannot be less than zero"})
    
    return jsonify({"power": base ** exp})
@app.route("/test/<int:x>")
def test(x):
    return {"value": x}

@app.route("/vote/<int:age>")
def vote(age):
    if age >= 18:
        return jsonify("you can vote")
    else:
        return jsonify("you can't vote")

@app.route
app.run()