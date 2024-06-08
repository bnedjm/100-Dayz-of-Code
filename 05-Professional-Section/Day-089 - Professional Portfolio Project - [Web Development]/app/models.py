from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditor, CKEditorField
from app import db


# Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# Add ToDoList
class AddTask(FlaskForm):
    add_task = SubmitField("Add Task")

# ToDoList
class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# Add ToDoList
class AddToDoList(FlaskForm):
    add_list = SubmitField("Add List")