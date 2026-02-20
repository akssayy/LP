from flask import Flask, jsonify

app = Flask(__name__)

users = [{"name": "Akshay"},
         {"name": "Waghral"}]


@app.route("/users/<int:index>", methods=["DELETE"])
def delete_user(index):
    if index < 0 or index >= len(users):
        return jsonify({"error": "Invalid index"}), 404

    deleted_user = users.pop(index) 

    return jsonify({"user delected": "sucessfully",
                    "delected": deleted_user}), 200  

app.run(debug=True)