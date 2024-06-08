from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField
from app import db


# Task
class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(250), nullable=False)
    starred = db.Column(db.Boolean, nullable=False)
    deadline = db.Column(db.String(250), nullable=False)
    list = db.relationship("ToDoList", back_populates="tasks")
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))

# ToDoList
class ToDoList(db.Model):
    __tablename__ = "lists"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    status = db.Column(db.String(250), nullable=False)
    deadline = db.Column(db.String(250), nullable=False)
    tasks = db.relationship("Task", back_populates="list")

# Add Task
class AddTask(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = CKEditorField("Description", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    starred = BooleanField("Do you want to star this task?")
    deadline = StringField("Deadline", validators=[DataRequired()])
    add_task = SubmitField("Add Task")

# Add ToDoList
class AddToDoList(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    deadline = StringField("Deadline", validators=[DataRequired()])
    add_list = SubmitField("Add List")

# Edit Task
class EditTask(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = CKEditorField("Description", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    starred = BooleanField("Do you want to star this task?")
    deadline = StringField("Deadline", validators=[DataRequired()])
    add_task = SubmitField("Update Task")

# Edit ToDoList
class EditToDoList(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    deadline = StringField("Deadline", validators=[DataRequired()])
    add_list = SubmitField("Update List")