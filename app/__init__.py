from flask import Flask, send_from_directory
from flask_restx import Api
from app.extensions import db, bcrypt, jwt
from app.api import api_bp
import config

def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(api_bp)

    @app.route('/')
    def index():
        return "Welcome to the HBNB API!"

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app
