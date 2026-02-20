from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {"id": 1, "name": "Akshay"},
  {"id": 2, "name": "Rahul"}
]

#next_id = 1

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200


    return jsonify({"error": "user not found"}), 404

app.run(debug=True)
