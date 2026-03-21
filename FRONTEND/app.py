from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    print("Received:", username, password)

    return jsonify({"message": "Login received"})

if __name__ == "__main__":
    app.run(debug=True)