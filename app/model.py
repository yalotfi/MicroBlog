from app import db


class User(db.Model):
    # Create a User table with fields id, nickname, and email
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        # How to print objects - use for debugging
        return '<User %r' % (self.nickname)
