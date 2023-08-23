from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['CKEDITOR_PKG_TYPE'] = 'full'
CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

class PostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired(), Length(max=250)])
    subtitle = StringField('Subtitle', validators=[DataRequired(), Length(max=250)])
    author = StringField('Your Name', validators=[DataRequired(), Length(max=250)])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), Length(max=250), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


@app.route("/", methods=['GET'])
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts), 200

# TODO: Add a route so that you can click on individual posts.
@app.route("/post/<int:post_id>", methods=['GET'])
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    return render_template("post.html", post=requested_post), 200

# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=['GET', 'POST']) # type: ignore
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
        title = form.title.data,
        subtitle = form.subtitle.data,
        body = form.body.data,   
        date = date.strftime(date.today(), "%B %d, %Y"),
        author = form.author.data,
        img_url = form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts")), 201
    return render_template("make-post.html", form=form), 200

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST']) # type: ignore
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)
    edit_form = PostForm(
        title = post_to_edit.title,
        subtitle = post_to_edit.subtitle,
        author = post_to_edit.author,
        img_url = post_to_edit.img_url,
        body = post_to_edit.body,
    )
    if edit_form.validate_on_submit():
        post_to_edit.title = edit_form.title.data
        post_to_edit.subtitle = edit_form.subtitle.data
        post_to_edit.body = edit_form.body.data
        post_to_edit.author = edit_form.author.data
        post_to_edit.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id)), 200
    return render_template("make-post.html", form=edit_form, edit=True), 200

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<int:post_id>") # type: ignore
def delete_post():
    return ""

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
