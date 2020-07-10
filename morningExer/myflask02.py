#!/usr/bin/env python3
from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

#grab the value 'username'
@app.route("/<username>")
def index(username):
    # render the jinja template "helloname.html"
    # apply the value of username for the var name
    return render_template("basic.html", name = username)

@app.route("/name")
def track(name):
    return "yo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

