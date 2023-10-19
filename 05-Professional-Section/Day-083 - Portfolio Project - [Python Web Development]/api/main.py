from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from smtplib import *
import requests
import os

EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
APP_PASSWORD = os.environ.get("APP_PASSWORD")
EMAIL_LIST = os.environ.get("EMAIL_LIST")

app = Flask(__name__)
Bootstrap5(app)

@app.route("/", methods=["GET", "POST"]) # type: ignore
def home():
    if request.method == "GET":
        return render_template("index.html"), 200
    elif request.method == "POST":
        subject = "New Contact request"
        data = request.form
        quote = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        with SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=EMAIL_SENDER, password=APP_PASSWORD) # type: ignore
            connect.sendmail(
                from_addr=EMAIL_SENDER, # type: ignore
                to_addrs=EMAIL_LIST, # type: ignore
                msg=f"Subject: {subject}\n\n"
                    f"{quote}"
            )
        return render_template("index.html"), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    