from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        new_user = User(
            email = request.form["email"],
            password = request.form["password"],
            name = request.form["name"]
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets", name=request.form["name"]))
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html", name=request.args.get("name"))


@app.route('/logout') # type: ignore
def logout():
    pass


@app.route('/download', methods=['GET']) # type: ignore
def download():
    return send_from_directory(
        directory="static",
        path="./files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
