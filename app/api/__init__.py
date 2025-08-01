from flask_restx import Api
from flask import Blueprint

from app.api.v1.amenities import api as amenity_ns
from app.api.v1.reviews import api as review_namespace

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='HBnB API', version='1.0', description='HBnB Application API')

api.add_namespace(amenity_ns, path='/amenities')
api.add_namespace(review_namespace, path='/reviews')


