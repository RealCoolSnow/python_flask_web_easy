from app.platform import db


class UserModel(db.Model):
    id = db.Column(db.Integer, nullable=False, doc='id', primary_key=True)
