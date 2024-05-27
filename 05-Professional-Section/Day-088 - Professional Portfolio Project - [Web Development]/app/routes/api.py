from flask import Blueprint, jsonify, request
from flask_httpauth import HTTPTokenAuth
from random import choice
from app import db
from app.models import Cafe

api_bp = Blueprint("api", __name__)
auth = HTTPTokenAuth(scheme="ApiKey")

# Example API key store
api_keys = {
    "your_api_key_1": "user1",
    "your_api_key_2": "user2",
    # Add more keys as needed
}

@auth.verify_token
def verify_api_key(api_key):
    if api_key in api_keys:
        return api_keys[api_key]
    return None

@api_bp.route("/random", methods=['GET']) # type: ignore
@auth.login_required
def random():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = choice(all_cafes)
    # return jsonify(
    #     cafe = {
    #         # "id": random_cafe.id,
    #         "name": random_cafe.name,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #         "map_url": random_cafe.map_url,   
    #         "amenities": {
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "has_sockets": random_cafe.has_sockets,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "seats": random_cafe.seats,
    #             "coffee_price": random_cafe.coffee_price
    #         }
    #         }
    #     )
    return jsonify(cafe=random_cafe.dictify()), 200

@api_bp.route("/all", methods=['GET']) # type: ignore
@auth.login_required
def all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.dictify() for cafe in all_cafes]), 200

@api_bp.route("/search", methods=['GET']) # type: ignore
@auth.login_required
def search():
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location==request.args.get("loc"))).scalars().all()
    if len(all_cafes) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"}), 404
    elif len(all_cafes) == 1:
        return jsonify(cafe=all_cafes[0].dictify()), 200
    else:
        return jsonify(cafes=[cafe.dictify() for cafe in all_cafes]), 200

@api_bp.route("/add", methods=['POST']) # type: ignore
@auth.login_required
def add():
    new_cafe = Cafe(
        name = request.form["name"],
        img_url = request.form["img_url"],
        location = request.form["location"],
        map_url = request.form["map_url"],   
        can_take_calls = bool(request.form["can_take_calls"]),
        has_sockets = bool(request.form["has_sockets"]),
        has_toilet = bool(request.form["has_toilet"]),
        has_wifi = bool(request.form["has_wifi"]),
        seats = request.form["seats"],
        coffee_price = request.form["coffee_price"]
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"}), 201

@api_bp.route("/update-price/<int:cafe_id>", methods=['PATCH']) # type: ignore
@auth.login_required
def update_price(cafe_id):
    try:
        cafe_to_update = db.get_or_404(Cafe, cafe_id)
    except:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database"}), 404
    else:
        cafe_to_update.coffee_price = request.args.get("coffee_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price"}), 200

@api_bp.route("/report-closed/<int:cafe_id>", methods=['DELETE']) # type: ignore
@auth.login_required
def report_closed(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        try:
            cafe_to_delete = db.get_or_404(Cafe, cafe_id) 
        except:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database"}), 404
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe"}), 200
    else:
        return jsonify(error={"Not Allowed": "Sorry, that's not allowed. Make sure you have the correct api-key"}), 403