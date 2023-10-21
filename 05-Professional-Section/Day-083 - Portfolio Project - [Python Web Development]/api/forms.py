from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    subject = StringField("Subject", validators=[DataRequired(), Length(max=100)])
    message = TextAreaField("Message", validators=[DataRequired()])
