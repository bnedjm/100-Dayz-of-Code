from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests


app = Flask(__name__)


@app.route("/")
def home():
    random_num = randint(0,9)
    current_year = datetime.today().year
    return render_template("index.html", num=random_num, year=current_year)

@app.route("/guess/<string:name>")
def guess(name):
    genderize_response = requests.get(url=f"https://api.genderize.io?name={name}")
    genderize_response.raise_for_status()
    gender_ = genderize_response.json()["gender"]
    agify_response = requests.get(url=f"https://api.agify.io?name={name}")
    agify_response.raise_for_status()
    age_ = agify_response.json()["age"]
    name_ = name.title()
    return render_template("guess.html", name=name_, gender=gender_, age=age_)


if __name__ == "__main__":
    app.run(debug=True)