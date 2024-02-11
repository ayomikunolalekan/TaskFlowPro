from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskflopro.db"
db = SQLAlchemy(app)

with app.app_context():
    
    class User(db.Model):
        first_name =  db.Column(db.String(50), nullable=False)
        last_name = db.Column(db.String(50), nullable=False)
        email = db.Column(db.String(128), unique=True, nullable=False, primary_key=True)
        password = db.Column(db.String(64), nullable=False)
        tasks = db.relationship("Task", backref = "user",  lazy=True)

        def __init__  (self, first_name, last_name, email, password):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password

    class Task(db.Model):
        id = db.Column(db.Integer, primary_key= True)
        title = db.Column(db.String(100), nullable= False)
        start = db.Column(db.DateTime, nullable= False, default=datetime.datetime.now())
        end = db.Column(db.DateTime, nullable= False)
        status = db.Column(db.String(100), nullable= False)
        user_id = db.Column(db.Integer, db.ForeignKey("user.email"), nullable= False)

        def __init__(self, title,start,end,status,user_id):
            self.title = title
            self.start = start
            self.end = end
            self.status = status
            self.user_id = user_id

    db.create_all()

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login", methods=["Get","Post"])
def login_page():
    return render_template("log_in.html")

@app.route("/signup", methods=["GET","POST"])
def signup_page():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password = request.form.get('password')
        confirm_password=request.form.get('confirmPassword')
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        db.session.add(user)
        db.session.commit()
    return render_template("sign_up.html")

@app.route("/dashboard")
def dashboard_page():
    #add task
    #remove task
    #
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

    