import csv
import os
from flask import Flask, session, render_template, request 
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'string'
#app.secret_key=os.environ.get('SECRET')
#app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("size.html")

@app.route("/Register", methods=["GET", "POST"])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Add user to database 
        users = Users(username=username,password=password)
        db.session.add(users)
        db.session.commit()
        return "Inserted into database"
    return render_template("register.html", form=reg_form)

@app.route("/error")
def error():
    return render_template("error.html")
