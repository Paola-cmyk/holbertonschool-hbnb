from flask import Flask
from flask_restx import Api
from app.extensions import db, bcrypt, jwt
from app.api import api_bp
import config

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to HBnB!'

from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)


    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(api_bp)

    return app
