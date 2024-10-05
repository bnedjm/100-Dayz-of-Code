import io
from flask import Blueprint, jsonify, render_template, request
from PIL import Image
from app.services.color_pallete_service import get_top_colors

web_bp = Blueprint('web', __name__)

@web_bp.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html"), 200

@web_bp.route("/colors", methods=['POST']) # type: ignore
def get_color_palette():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    
    image = Image.open(io.BytesIO(file.read()))

    try:
        colors = get_top_colors(image)
    except Exception as e:
        return jsonify({'error': f'An error occured while processing the image: {e}'}), 400
    
    return jsonify(colors), 200
