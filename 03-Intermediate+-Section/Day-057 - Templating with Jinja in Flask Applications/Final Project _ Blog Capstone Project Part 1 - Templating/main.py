from flask import Flask, render_template
import requests


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
response.raise_for_status()
data = response.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=data)

@app.route("/posts/<int:id>")
def posts(id):
    return render_template("post.html", posts=data, id=id)

if __name__ == "__main__":
    app.run(debug=True)
