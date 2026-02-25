from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
#create database
with app.app_context():
    db.create_all()


@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name required"}), 400 

    new_user = User(name=data["name"])

    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        "message": "User created",
        "id": new_user.id,
        "name": new_user.name
    }), 201

app.run(debug=True)