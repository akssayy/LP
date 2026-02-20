from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
next_id = 1

@app.route("/users", methods=["POST"])
def create_user():
    global next_id   # MUST be here

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name required"}), 400

    new_user = {
        "id": next_id,
        "name": data["name"]
    }

    users.append(new_user)
    next_id += 1

    return jsonify(new_user), 201

app.run(debug=True)
