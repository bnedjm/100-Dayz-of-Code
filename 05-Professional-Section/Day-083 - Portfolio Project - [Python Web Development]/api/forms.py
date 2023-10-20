from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    subject = PasswordField("Subject", validators=[DataRequired(), Length(max=100)])
    message = PasswordField("Message", validators=[DataRequired()])
    submit = SubmitField("Contact me")