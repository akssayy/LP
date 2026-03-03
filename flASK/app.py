from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(50))

    posts = db.relationship('Post', backref='user')


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))

    content = db.Column(db.String(500))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )


with app.app_context():

    db.create_all()

    # Insert data ONLY if database empty
""" if User.query.first() is None:

        user1 = User(
            name="Akshay",
            email="akshay@email.com"
        )

        db.session.add(user1)
        db.session.commit()

        post1 = Post(
            title="First Post",
            content="Hello",
            user_id=user1.id
        )

        post2 = Post(
            title="Second Post",
            content="World",
            user_id=user1.id
        )

        db.session.add(post1)
        db.session.add(post2)

        db.session.commit()


    posts = Post.query.all()

    for post in posts:

        print(post.title)

        print(post.user.name)"""

with app.app_context():

    db.create_all()

    user = User.query.first()

    if user:
        for post in user.posts:
            print(post.title)

    posts = Post.query.all()

    for post in posts:

        print(post.title)

        print(post.user.name)

@app.route("/posts")
def get_posts():

    posts = Post.query.all()

    result =[]

    for post in posts:

        result.append({
            "title": post.title,
            "content": post.content,
            "author": post.user.name
        })

    return jsonify(result)

app.run()