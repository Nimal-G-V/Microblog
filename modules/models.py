from modules import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(200))
    posts = db.relationship("Posts", backref="author", lazy="dynamic")

    def __repr__(self):
        return f"<id : { self.id }>\n<username : { self.username }>\n<email : { self.email }>"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<id : { self.id }>\n<content: { self.content }>\n<time stamp : { self.time_stamp }>"
