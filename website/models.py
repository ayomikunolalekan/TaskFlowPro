import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import db
# from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    first_name =  db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    tasks = db.relationship("Task", backref = "user",  lazy=True)

    def __init__  (self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Task(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable= False)
    start = db.Column(db.DateTime, nullable= False)
    end = db.Column(db.DateTime, nullable= False)
    status = db.Column(db.String(100), nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False)

    def __init__(self, title, start, end, status, user_id):
        self.title = title
        self.start = start
        self.end = end
        self.status = status
        self.user_id = user_id

