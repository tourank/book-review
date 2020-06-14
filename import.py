import os
from flask import Flask, session, render_template, request 
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

users = db.execute("SELECT username, password FROM usernames").fetchall() # execute this SQL command and return all of the results
for user in users:

    print(f"{user.username} and {user.password}")

f = open("users.csv")
reader = csv.reader(f)

for username, password in reader:
    db.execute("INSERT INTO usernames (username, password) VALUES (:username, :password)",
            {"username": username, "password": password})
db.commit()



