from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '$874d84bbabfae28eb9d6747ec8'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST']) # type: ignore
def register():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user:
            return redirect(url_for("register"))
        else:
            new_user = User(
                email = request.form["email"],
                password = generate_password_hash(request.form["password"], method="pbkdf2:sha256", salt_length=8),
                name = request.form["name"]
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user:
            if check_password_hash(user.password, request.form["password"]):
                login_user(user)
                return redirect(url_for("secrets", name=user.name))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=request.args.get("name"))


@app.route('/logout', methods=['GET', 'POST']) # type: ignore
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download', methods=['GET']) # type: ignore
@login_required
def download():
    return send_from_directory(
        directory="static",
        path="./files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
