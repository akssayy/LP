from flask import request, jsonify
from app import app, db
from models import User
from schemas import user_schema, users_schema


@app.route("/")
def home():
    return "API WORKING"

@app.route("/users", methods=["POST"])
def create_user():

    data = user_schema.load(request.json)

    user = User(
        name=data["name"],
        age=data["age"],
        email=data["email"]
    )

    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 201

@app.route("/users", methods=["GET"])
def get_users():

    users = User.query.all()

    return users_schema.dump(users)


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):

    user = User.query.get(id)

    if not user:
        return {"error": "User not found"}, 404

    return user_schema.dump(user)

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):

    user = User.query.get(id)

    if not user:
        return {"error": "User not found"}, 404

    data = user_schema.load(request.json)

    user.name = data["name"]
    user.age = data["age"]
    user.email = data["email"]

    db.session.commit()

    return user_schema.dump(user)

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    user = User.query.get(id)

    if not user:
        return {"error": "User not found"}, 404

    db.session.delete(user)
    db.session.commit()

    return {"message": "User deleted"}