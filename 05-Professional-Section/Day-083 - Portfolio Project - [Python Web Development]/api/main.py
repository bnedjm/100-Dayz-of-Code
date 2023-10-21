from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm
from smtplib import SMTP
import os


# ENV VARS
EMAIL = os.environ.get("EMAIL_SENDER")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

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
def notify(request : Contacts):
    notification = f"Subject: {request.id} | {request.name} | {request.subject}\n\n{request.message}"
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
        notify(new_contact_request)
        db.session.commit()
        return redirect(url_for("home")+"#work"), 201 # type: ignore

    elif request.method == "POST":

        # flash(error)
        # return redirect(url_for("home")+"#contact"), 303
        return render_template("index.html", form=contact_form), 303

    
    return render_template("index.html", form=contact_form), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
    