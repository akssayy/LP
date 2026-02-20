from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
next_id = 1


@app.route("/users/<string:value>", methods=["DELETE"])
def delete_user(value):
    for user in users:
        if user["name"] == value:
            users.remove(user)
            return jsonify({"message": "Deleted Successfully",
                            "deleted_user": user}), 200
        
    return jsonify({"error": "user not found"}), 404  

app.run(debug=True)