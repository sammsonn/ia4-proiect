from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note (db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key
    data = db.Column(db.String(10000)) # string of max length 10000
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # date and time
    user_id = db.Column(db.Integer, db.ForeignKey("user.id")) # foreign key

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key
    email = db.Column(db.String(150), unique=True) # unique email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note") # one to many relationship