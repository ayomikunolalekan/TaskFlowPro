from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login")
def login_page():
    return render_template("log_in.html")

@app.route("/signup")
def signup_page():
    return render_template("sign_up.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")