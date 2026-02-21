from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  """{"id": 1, "name": "Akshay"},
  {"id": 2, "name": "Rahul"}"""
]

#next_id = 1

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    if "name" not in data:
        return jsonify({"error": "Name field is required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            return jsonify(user), 200

    return jsonify({"error": "User not found"}), 404

@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    return jsonify(data)


app.run(debug=True)
