from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_cors import CORS
from config import Config
import os

SECRET_KEY = os.urandom(32)

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = SECRET_KEY

    ckeditor = CKEditor(app)
    Bootstrap5(app)
    CORS(app)

    from app.routes.web import web_bp

    app.register_blueprint(web_bp)

    return app
