from flask import Blueprint, render_template, redirect, url_for
from app.models import ToDoList, Task, AddToDoList, AddTask, EditToDoList, EditTask
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
        title = form.title.data,
        status = form.status.data,
        deadline = form.deadline.data
        )
        db.session.add(new_list)
        db.session.commit()
        return redirect(url_for("web.home")), 201
    return render_template("ops.html", form=form, is_edit=False, is_list=True), 200

# Edit a To-Do List
@web_bp.route("/list/edit/<int:list_id>", methods=['GET', 'POST'])
def edit_list(list_id):
    list_to_edit = db.get_or_404(ToDoList, list_id)
    form = EditToDoList(
        title = list_to_edit.title,
        status = list_to_edit.status,
        deadline = list_to_edit.deadline
    )
    if form.validate_on_submit():
        list_to_edit.title = form.title.data
        list_to_edit.status = form.status.data
        list_to_edit.deadline = form.deadline.data
        db.session.commit()
        return redirect(url_for("web.show_list", list_id=list_id)), 201
    return render_template("ops.html", form=form, is_edit=True, is_list=True), 200

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
@web_bp.route("/task/add/<int:list_id_>", methods=['GET', 'POST'])
def add_task(list_id_):
    form = AddTask()
    if form.validate_on_submit():
        new_task = Task(
            title = form.title.data,
            description = form.description.data,
            status = form.status.data,
            starred = form.starred.data,
            deadline = form.deadline.data,
            list_id = list_id_
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("web.show_list", list_id=list_id_)), 201
    return render_template("ops.html", form=form, is_edit=False, is_list=False), 200

# Edit a task in a To-Do List
@web_bp.route("/task/edit/<int:task_id>", methods=['GET', 'POST'])
def edit_task(task_id):
    task_to_edit = db.get_or_404(Task, task_id)
    form = EditTask(
        title = task_to_edit.title,
        description = task_to_edit.description,
        status = task_to_edit.status,
        starred = task_to_edit.starred,
        deadline = task_to_edit.deadline
    )
    if form.validate_on_submit():
        task_to_edit.title = form.title.data
        task_to_edit.description = form.description.data
        task_to_edit.status = form.status.data
        task_to_edit.starred = form.starred.data
        task_to_edit.deadline = form.deadline.data
        db.session.commit()
        return redirect(url_for("web.show_task", task_id=task_id)), 201
    return render_template("ops.html", form=form, is_edit=True, is_list=False), 200

# Delete a task from a To-Do List
@web_bp.route("/task/delete/<int:task_id>")
def delete_task(task_id):    
    task_to_delete = db.get_or_404(Task, task_id) 
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("web.home")), 204