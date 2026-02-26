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


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = sqlite3.connect("instance/users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id=?", (id,))
    user = cursor.fetchone()

    conn.close()

    if user:
         return {
             "id": user[0],
             "name": user[1] }
    else:   
        return jsonify({"message ": "user not found"}), 404 

    
    
   

app.run(debug=True)