from flask import Flask, render_template
import requests


blog_url = "https://api.npoint.io/a90e355e335f23e642d3"
response = requests.get(url=blog_url)
response.raise_for_status()
data = response.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/posts/<int:id>")
def posts(id):
    for post in data:
        if post["id"] == id:
            read_more_post = post
    return render_template("post.html", post=read_more_post)


if __name__ == "__main__":
    app.run(debug=True)
