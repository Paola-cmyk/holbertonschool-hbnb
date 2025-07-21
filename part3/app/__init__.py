from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import DevelopmentConfig

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    # Example: Register blueprints here
    # from app.routes.auth import auth_bp
    # app.register_blueprint(auth_bp)

    return app
