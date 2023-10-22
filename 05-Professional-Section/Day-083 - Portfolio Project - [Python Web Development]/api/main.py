from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures  import MultiDict
from forms import ContactForm
from smtplib import SMTP
from dotenv import load_dotenv
import os


# ENV VARS
load_dotenv(".env")
EMAIL = os.environ.get("EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")

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

# FUNCs
def notify_admin(request : Contacts):
    notification = f"Subject: {request.id:04d} | {request.name} | {request.subject}\n\n{request.message}"
    with SMTP("smtp.gmail.com", port=587) as connect:
        connect.starttls()
        connect.login(user=EMAIL, password=APP_PASSWORD) # type: ignore
        connect.sendmail(
            from_addr=EMAIL, # type: ignore
            to_addrs=ADMIN_EMAIL, # type: ignore
            msg=notification
        )

def notify_requester(request : Contacts):
    notification = f"Subject: {request.id:04d} | Thank you for reaching out!\n\nYour contact request has been received. I will get back to you as soon as possible. In the meantime, I invite you to check my work."
    requester_email = request.email
    with SMTP("smtp.gmail.com", port=587) as connect:
        connect.starttls()
        connect.login(user=EMAIL, password=APP_PASSWORD) # type: ignore
        connect.sendmail(
            from_addr=EMAIL, # type: ignore
            to_addrs=requester_email, # type: ignore
            msg=notification
        )

# ROUTES
@app.route("/", methods=["GET", "POST"]) # type: ignore
def home():
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        new_contact_request = Contacts(
            name = contact_form.name.data,
            email = contact_form.email.data,
            subject = contact_form.subject.data,
            message = contact_form.message.data
        ) # type: ignore
        db.session.add(new_contact_request)
        db.session.commit()
        notify_admin(new_contact_request)
        notify_requester(new_contact_request)
        return redirect(url_for("home")), 201 # type: ignore

    elif contact_form.is_submitted() and not contact_form.validate():
        if "Invalid email address." not in contact_form.email.errors:
            error = "All fields must be filled"
        else:
            error = "Invalid email address"
        flash(error)
        session["contactFormData"] = request.form
        return redirect(url_for("home")+"#contact"), 303
    
    contactFormData = session.get("contactFormData", None)
    if contactFormData:
        contact_form = ContactForm(MultiDict(contactFormData))
        contact_form.validate()
        session.pop("contactFormData")
    return render_template("index.html", form=contact_form), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
    