from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Task
from datetime import datetime
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def dashboard_page():
    tasks = Task.query.join(User).filter(User.email == current_user.email).all()
    return render_template("dashboard.html", user=current_user, tasks=tasks)

@views.route("/create_task", methods=["GET", "POST"])
@login_required
def create_task():
    if request.method == "POST":
        title = request.form.get("title")
        start_date = request.form.get("startDate")
        # Start date conversion
        new_start_date = start_date.replace('T', ' ')
        startDate = datetime.strptime(new_start_date, '%Y-%m-%d %H:%M')
        updatedstartDate = startDate

        due_date = request.form.get("dueDate")
        # Due date conversion
        due_date = due_date.replace('T', ' ')
        dueDate = datetime.strptime(due_date, '%Y-%m-%d %H:%M')
        updatedDueDate = dueDate

        if not title:
            flash("Task title must not be empty!", category="error")
        else:
            task = Task(title=title, start=updatedstartDate, end=updatedDueDate, status="uncompleted", user_id=current_user.id)
            db.session.add(task)
            db.session.commit()
            flash("Task Created!", category="success")
            return redirect(url_for("views.dashboard_page"))
    return render_template("create_task.html", user=current_user)


@views.route("/delete_task/<id>")
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id).first()

    if not task:
        flash("Task does not exist", category="error")
    else:
        db.session.delete(task)
        db.session.commit()
    
    return redirect(url_for("views.dashboard_page"))

