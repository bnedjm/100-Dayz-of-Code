from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

app = Flask(__name__)
app.secret_key = "HsereIsASecretKey"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def login():
    form = MyForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
