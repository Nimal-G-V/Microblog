from modules import app
from flask import render_template, flash, redirect, url_for, request
from modules.forms import LoginForm
from modules.variables import user, posts
from modules.models import Users
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route("/")
@login_required
def home():
    return render_template("index.html", title="Home", posts=posts)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Username or password is incorrect.")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page and url_parse(next_page).netloc != "":
            return redirect(url_for("home"))
        return redirect(next_page)
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))