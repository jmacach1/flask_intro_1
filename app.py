#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

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
    return me
