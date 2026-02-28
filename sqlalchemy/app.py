from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route("/users", methods=["GET"])
def get_user():

    users = User.query.all()

    if not users:
        return jsonify({"error": "user not found"}), 404
    
    result = []

    for user in users:
        result.append({
            "id": user.id,
            "name": user.name
        })

    total_user = len(result)

    return jsonify({"total users are":total_user,
                    "users":result
                })



# ...existing code...
# @app.route("/users", methods=["POST"])
# def create_user():
#
#     data = request.json
#
#     if not data or "name" not in data:
#         return jsonify({"error": "name required"}), 400
#
#     new_user = User(name=data["name"])
#     db.session.add(new_user)
#     db.session.commit()
#
#     return jsonify({"message": "user created"}), 200
# ...existing code...


app.run(debug=True)