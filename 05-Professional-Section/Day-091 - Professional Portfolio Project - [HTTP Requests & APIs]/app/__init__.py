from flask import Flask
from config import Config
from app.routes.api import UPLOAD_FOLDER
import os

SECRET_KEY = os.urandom(32)

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = SECRET_KEY
 
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    from app.routes.api import api_bp

    app.register_blueprint(api_bp, url_prefix='/api')

    return app
