from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = result.scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        with app.app_context():
            book = Books(
                title = request.form['title'],
                author = request.form['author'],
                rating = float(request.form['rating'])
                )
            db.session.add(book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<int:index>", methods = ['GET','POST']) # type: ignore
def edit(index):
    with app.app_context():
        book_to_update = db.get_or_404(Books, index) 
        if request.method == "POST":
            book_to_update.rating = request.form['new_rating']
            db.session.commit()
            return redirect(url_for("home"))
        else:
            return render_template("edit.html", index=index, book=book_to_update)


@app.route("/delete/<int:index>") # type: ignore
def delete(index):
    with app.app_context():
        book_to_delete = db.get_or_404(Books, index) 
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

