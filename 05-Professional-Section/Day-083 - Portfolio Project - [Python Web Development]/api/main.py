from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from smtplib import SMTP
import os
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from forms import ContactForm

# ENV VARS
EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
APP_PASSWORD = os.environ.get("APP_PASSWORD")
EMAIL_LIST = os.environ.get("EMAIL_LIST")

# FLASK APP
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy()
db.init_app(app)

class Contacts(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

# ROUTES
@app.route("/", methods=["GET", "POST"]) # type: ignore
def home():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        # quote = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        # with SMTP("smtp.gmail.com", port=587) as connect:
        #     connect.starttls()
        #     connect.login(user=EMAIL_SENDER, password=APP_PASSWORD) # type: ignore
        #     connect.sendmail(
        #         from_addr=EMAIL_SENDER, # type: ignore
        #         to_addrs=EMAIL_LIST, # type: ignore
        #         msg=f"Subject: {}\n\n"
        #             f"{quote}"
        #     )
        new_contact_request = Contacts(
            name = contact_form.name.data,
            email = contact_form.email.data,
            subject = contact_form.subject.data,
            message = contact_form.message.data
        ) # type: ignore
        db.session.add(new_contact_request)
        db.session.commit()
        return redirect(url_for("home")), 201

    return render_template("index.html", form=contact_form), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
    