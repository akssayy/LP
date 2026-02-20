from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {"id": 1, "name": "Akshay"},
  {"id": 2, "name": "Rahul"}
]

#next_id = 1

@app.route("/users", methods=["GET"])
def get_all_user():
    return jsonify({"count": len(users),
                    "users": users}), 200
    

app.run(debug=True)
