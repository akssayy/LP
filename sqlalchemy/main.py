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


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"error":"User not found"}),404

    db.session.delete(user)

    db.session.commit()

    return jsonify({"message":"User deleted"}),200

    
    
   

app.run(debug=True)