from flask import Flask
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

    new_user = User(name="Akshay")

    db.session.add(new_user)
    db.session.commit()

app.run(debug=True)