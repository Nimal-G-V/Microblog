from modules import app
from flask import render_template, flash, redirect, url_for
from modules.forms import LoginForm
from modules.variables import user, posts

@app.route("/")
def home():
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested, user:{ form.username.data } and remeber me:{ form.remember_me.data }.")
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)