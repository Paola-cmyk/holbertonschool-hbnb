from flask import Flask
from flask_restx import Api
from app.extensions import db, bcrypt, jwt
from app.api import api_bp
import config

def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register Blueprint
    app.register_blueprint(api_bp)

    return app
