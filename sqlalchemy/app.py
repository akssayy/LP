from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route("/users", methods=["POST"])
def create_user():

    data = request.json

    if not data or "name" not in data:
        return jsonify({"error": "name required"}), 400

    new_user = user(name=data["name"])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "user created"}), 200

app.run(debug=True)