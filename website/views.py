from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Task, CompletedTask
from datetime import datetime
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def dashboard_page():
    tasks = Task.query.join(User).filter(User.email == current_user.email).all()
    return render_template("dashboard.html", user=current_user, tasks=tasks)


@views.route("/active_task")
@login_required
def active_task():
    tasks = Task.query.join(User).filter(User.email == current_user.email).all()
    return render_template("active_tasks.html", user=current_user, tasks=tasks)


@views.route("/completed_task")
@login_required
def completed_task():
    tasks = Task.query.join(User).filter(User.email == current_user.email).all()
    return render_template("completed_task.html", user=current_user, tasks=tasks)

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

@views.route("/complete_task/<id>")
@login_required
def mark_as_completed(id):
    task = Task.query.filter_by(id=id).first()

    if not task:
        flash("Task does not exist", category="error")
    else:
        task.status = "completed"

        complete_task = CompletedTask(title=task.title, start=task.start, end=task.end, status="completed", user_id=current_user.id)
        db.session.add(complete_task)
        
        # Remove the task from the Task table
        db.session.delete(task)

        db.session.commit()
        flash("Completed Task !", category="success")
        return redirect(url_for("views.completed_task"))
    

@views.route("/edit_task/<id>" , methods = ["GET","POST"])
@login_required
def edit_task(id):
    task = Task.query.filter_by(id=id).first()

    if not task:
        flash("Task does not exist", category="error")
    elif request.method == "POST":
        title = request.form.get("title")
        start_date = request.form.get("startDate")
        due_date = request.form.get("dueDate")
        # Start date conversion
        start_date = start_date.replace('T', ' ')
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')

        # Due date conversion
        due_date = due_date.replace('T', ' ')
        due_date = datetime.strptime(due_date, '%Y-%m-%d %H:%M')

        #update task
        task.title = title
        task.start = start_date
        task.end = due_date

        db.session.add(task)
        db.session.commit()
        flash("Task updated!", category="success")
        return redirect(url_for("views.dashboard_page"))
    else:
        return render_template("edit_task.html", task = task, task_url=f"/edit_task/{id}")

@views.route("/delete_task/<id>")
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id).first()

    if not task:
        flash("Task does not exist", category="error")
    else:
        db.session.delete(task)
        db.session.commit()
    
    return redirect(url_for("views.active_task"))

@views.route("/delete_completed_task/<id>")
@login_required
def delete_completed_task(id):
    task = CompletedTask.query.filter_by(id=id).first()

    if not task:
        flash("Task does not exist", category="error")
    else:
        db.session.delete(task)
        db.session.commit()
    
    return redirect(url_for("views.completed_task"))

