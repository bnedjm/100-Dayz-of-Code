from flask import Blueprint, render_template, redirect, url_for
from app.models import ToDoList, Task, AddToDoList, AddTask
from app import db


web_bp = Blueprint('web', __name__)

# Homepage
@web_bp.route("/")
def home():
    lists = db.session.execute(db.select(ToDoList)).scalars().all()
    return render_template("index.html", all_lists=lists), 200

################################################ TO-DO List ################################################

# Show a specific To-Do List
@web_bp.route("/list/<int:list_id>")
def show_list(list_id):
    requested_list = db.session.execute(db.select(ToDoList).where(ToDoList.id==list_id)).scalar()
    return render_template("list.html", list=requested_list), 200

# Add a To-Do List
@web_bp.route("/list/add", methods=['GET', 'POST'])
def add_list():
    form = AddToDoList()
    if form.validate_on_submit():
        new_list = ToDoList(
        # TBD
        )
        db.session.add(new_list)
        db.session.commit()
        return redirect(url_for("web.home")), 201
    return render_template("add-list.html", form=form), 200

# Edit a To-Do List
@web_bp.route("/list/edit/<int:list_id>", methods=['GET', 'POST'])
def edit_list(list_id):
    form = AddToDoList()
    if form.validate_on_submit():
        list_to_edit = db.get_or_404(ToDoList, list_id)
        list_to_edit = ToDoList(
            # TBD
        )
        db.session.commit()
        return redirect(url_for("web.home")), 201
    return render_template("edit-list.html", form=form), 200

# Delete a To-Do List
@web_bp.route("/list/delete/<int:list_id>")
def delete_list(list_id):    
    list_to_delete = db.get_or_404(ToDoList, list_id) 
    db.session.delete(list_to_delete)
    db.session.commit()
    return redirect(url_for("web.home")), 204

################################################ TO-DO Task ################################################

# Show a specific Task
@web_bp.route("/task/<int:task_id>")
def show_task(task_id):
    requested_task = db.session.execute(db.select(Task).where(Task.id==task_id)).scalar()
    return render_template("task.html", task=requested_task), 200

# Add a task to a To-Do List
@web_bp.route("/task/add", methods=['GET', 'POST'])
def add_task():
    form = AddTask()
    if form.validate_on_submit():
        new_task = Task(
        # TBD
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("web.home")), 201
    return render_template("add-task.html", form=form), 200

# Edit a task in a To-Do List
@web_bp.route("/task/edit/<int:task_id>", methods=['GET', 'POST'])
def edit_task(task_id):
    form = AddTask()
    if form.validate_on_submit():
        task_to_edit = db.get_or_404(Task, task_id)
        task_to_edit = Task(
            # TBD
        )
        db.session.commit()
        return redirect(url_for("web.home")), 201
    return render_template("edit-task.html", form=form), 200

# Delete a task from a To-Do List
@web_bp.route("/task/delete/<int:task_id>")
def delete_task(task_id):    
    task_to_delete = db.get_or_404(Task, task_id) 
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("web.home")), 204