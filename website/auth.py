from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # user = current_app.db.session.query(current_app.User).filter_by(email=email).first()
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("User logged in successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.dashboard_page"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("User does not exist", category="error")

    return render_template("log_in.html", user=current_user)

@auth.route("/signup", methods=["GET", "POST"])
def signup_page():
    if request.method == "POST":
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(firstName) < 3:
            flash("First name must be at least 3 letters", category="error")
        elif len(lastName) < 3:
            flash("Last name must be at least 3 letters", category="error")
        elif password != confirmPassword:
            flash("Passwords do not match!", category="error")
        elif len(password) < 8:
            flash("Password must be at least 8 characters")
        else:
            new_user = User(first_name=firstName, last_name=lastName, email=email, password=generate_password_hash(password, "scrypt"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created successfully", category="success")
            return redirect(url_for("views.dashboard_page"))

    return render_template("sign_up.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login_page"))