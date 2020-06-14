from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()
class Users(db.Model):

    _tablename_ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
