#!/usr/bin/env python3

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from database import User

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/about")
def about():
    me = {
        "first_name" : "Jerald",
        "last_name" : "Macachor",
        "hobbies" : [ 
            "Brazilian Jiu Jitsu",
            "Salsa Bachata Dancing",
            "Surfing"
        ],
        "isCool" : True
    }
    return render_template("about.html", user=me)

@app.route("/about/<int:uid>")
def aboutUser(uid):
    user = User.query.filter_by(id=uid).first()
    return render_template("about.html", user=user)

@app.errorhandler(404)
def page_not_found(e): # e means exception
    return render_template("404.html"), 404 # returns tuple, page and status