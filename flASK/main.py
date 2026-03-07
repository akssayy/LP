from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/users", methods=["POST"])
def create_user():

    data = request.json

    name = data.get("name")
    age = data.get("age")

    if name is None or age is None:
        return jsonify({"error": "name and age is required"}), 400

    if name.strip() == "":
        return jsonify({"error": "name cannot be empty"}), 400

    if not isinstance(age, int):
        return jsonify({"error": "age must be a number"}), 400

    user = {
        "id": len(users) + 1,
        "name": name,
        "age": age
    }

    users.append(user)

    return jsonify(user), 201

app.run(debug=True)