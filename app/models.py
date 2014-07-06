from datetime import datetime
from app import db


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    body = db.Column(db.String(500), nullable = False)
    post_date = db.Column(db.Date, nullable=False)
    edited_date = db.Column(db.Date)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.post_date = datetime.utcnow()

    def __repr__(self):
        return '{post.title} - posted on: {post.post_date}'.format(post=self)

    def modify_post(self, title, body):
        self.title = title
        self.body = body
        self.edited_date = datetime.utcnow()