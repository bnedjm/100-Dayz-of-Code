from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from config import Config
import os

SECRET_KEY = os.urandom(32)
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = SECRET_KEY

    db.init_app(app)
    Bootstrap5(app)

    from app.routes.web import web_bp
    from app.routes.api import api_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
