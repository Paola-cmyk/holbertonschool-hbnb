from flask import Blueprint
from flask_restx import Api

# Create blueprint and API instance
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp, title='HBnB API', version='1.0', description='HBnB Application API')

# Import namespaces
from app.api.v1.auth import api as auth_ns
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.protected import api as protected_ns

# Add namespaces
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(users_ns, path='/users')
api.add_namespace(amenities_ns, path='/amenities')
api.add_namespace(reviews_ns, path='/reviews')
api.add_namespace(protected_ns, path='/protected')
