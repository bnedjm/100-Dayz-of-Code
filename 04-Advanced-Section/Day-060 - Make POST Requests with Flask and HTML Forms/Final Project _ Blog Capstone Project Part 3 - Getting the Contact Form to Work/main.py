from flask import Flask, render_template, request
from smtplib import *
import requests
import os

EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
APP_PASSWORD = os.environ.get("APP_PASSWORD")
EMAIL_LIST = os.environ.get("EMAIL_LIST")

posts = requests.get("https://api.npoint.io/a90e355e335f23e642d3").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", method=request.method)
    elif request.method == "POST":
        subject = "New Contact request"
        data = request.form
        quote = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        with SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=EMAIL_SENDER, password=APP_PASSWORD)
            connect.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=EMAIL_LIST,
                msg=f"Subject: {subject}\n\n"
                    f"{quote}"
            )
        return render_template("contact.html", method=request.method)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
