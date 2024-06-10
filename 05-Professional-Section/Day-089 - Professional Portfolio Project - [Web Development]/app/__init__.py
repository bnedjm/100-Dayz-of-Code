from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from config import Config
import os

SECRET_KEY = os.urandom(32)
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = SECRET_KEY

    ckeditor = CKEditor(app)
    Bootstrap5(app)
    db.init_app(app)
    

    from app.routes.web import web_bp

    app.register_blueprint(web_bp)

    return app
