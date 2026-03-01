from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(50))

class post(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))

    content = db.Column(db.String(500))

    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))

with app.app_context():
    db.create_all()

    user1 = User(
        name = "Akshay",
        email = "akshay@email.com"
    ) 

    db.session.add(user1)
    db.session.commit()

    post1 = post(
        title = "First post",
        content = "world",
        user_id=1
    )

    post2 = post(
        title = "Second Post",
        content = "World",
        user_id=1
    )

    db.session.add(post1)
    db.session.add(post2)

    db.session.commit()

    users = User.query.all()

    for user in users:
        print(user.name, user.email)

    posts = post.query.all()

    for post in posts:
        print(post.title, "belongs to", post.user_id)

app.run()