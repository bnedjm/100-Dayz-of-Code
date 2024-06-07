from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditor, CKEditorField
from app import db

# APIKey | TBD
class APIKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), unique=True, nullable=False)
    user = db.Column(db.String(255), nullable=False)

# User | TBD
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Cafe
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def dictify(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
class AddCafe(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired(), Length(max=250)])
    map_url = StringField('Map URL', validators=[DataRequired(), Length(max=500), URL()])
    img_url = StringField('Image URL', validators=[DataRequired(), Length(max=500), URL()])
    location = StringField('Location', validators=[DataRequired(), Length(max=250)])
    seats = StringField('Seats', validators=[DataRequired(), Length(max=250)])
    has_toilet = BooleanField('Has Toilet?', validators=[DataRequired()])
    has_wifi = BooleanField('Has Wifi?', validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets?', validators=[DataRequired()])
    can_take_calls = BooleanField('Can Take Calls?', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired(), Length(max=250)])
    add_cafe = SubmitField('Add Cafe')