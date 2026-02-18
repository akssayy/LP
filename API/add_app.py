from flask import Flask, jsonify

app = Flask(__name__)

users = []

@app.route("/power/<int:base>/<int:exp>")
def power(base, exp):
    if exp < 0 :
        return jsonify({"error": "exp cannot be less than zero"})
    
    return jsonify({"power": base ** exp})

app.run()