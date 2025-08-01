from flask_restx import Api
from flask import Blueprint
from .v1.amenities import api as amenity_ns

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='HBnB API', version='1.0', description='HBnB Application API')

api.add_namespace(amenity_ns, path='/amenities')

from api import reviews as review_namespace

api.add_namespace(review_namespace, path='/api/v1/reviews')

