from sqlite3 import dbapi2
from app import db

# The User class inherits from db.Model (a base class for all models from Flask-SQLAlchemy)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # Fields are created above as instances of the db.Column class, which take the field type as an argument, plus optional ones

    def __repr__(self):
        return '<User {}>'.format(self.username)
