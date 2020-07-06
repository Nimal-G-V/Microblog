from modules import app
from flask import render_template
from modules.variables import user, posts

@app.route("/")
def home():
    return render_template("index.html", title="Home", user=user, posts=posts)