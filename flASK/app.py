from flask import Flask

app = Flask(__name__)

#fake database
users = {1:{"name": "Aksh", "balance": 5000},
2: {"name": "sam", "balance": 3000}}


@app.route("/user/<int:user_id>")
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "user not found"})

app.run()