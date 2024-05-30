from flask import Blueprint, render_template, redirect, url_for
from app.models import Cafe, AddCafe
from app import db


web_bp = Blueprint('web', __name__)

@web_bp.route("/")
def home():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return render_template("index.html", all_cafes=cafes), 200

@web_bp.route("/cafe/<int:cafe_id>")
def show(cafe_id):
    requested_cafe = db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
    return render_template("cafe.html", cafe=requested_cafe), 200

@web_bp.route("/add", methods=['GET', 'POST'])
def add():
    form = AddCafe()
    if form.validate_on_submit():
        new_cafe= Cafe(
        name = form.name.data,
        map_url = form.map_url.data,
        img_url = form.img_url.data,
        location = form.location.data,
        seats = form.seats.data,
        has_toilet = bool(form.has_toilet.data),
        has_wifi = bool(form.has_wifi.data),
        has_sockets = bool(form.has_sockets.data),
        can_take_calls = bool(form.can_take_calls.data),
        coffee_price = form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home")), 201
    return render_template("add-cafe.html", form=form), 200

@web_bp.route("/delete/<int:cafe_id>")
def delete(cafe_id):    
    cafe_to_delete = db.get_or_404(Cafe, cafe_id) 
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for("home")), 204