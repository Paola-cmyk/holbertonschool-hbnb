from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email address of the user'),
    'is_admin': fields.Boolean(required=True, description='Admin status of the user'),
    'password': fields.String(required=True, description='User password')
})

update_user_model = api.model('UpdateUser', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.Boolean(description='Email address of the user')
})
@api.route('/')

class UserRegistrationResource(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered or invalid input')
    def post(self):

        """registering a new user"""

        user_data = api.payload
        user_data['email'] = user_data['email'].strip().lower()

        if facade.get_user_by_email(user_data['email']):
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email,
            'is_admin': new_user.is_admin
        }, 201

@api.route('/<user_id>')

class UserDetailResource(Resource):
    @jwt_required()
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):

        """retrieving user details by ID"""

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

@api.route('/user-list')

class UserListResource(Resource):
    @jwt_required()
    @api.response(200, 'List of users retrieved successfully')
    def get(self):

        """retrieving a list of all users (authentication required)"""

        users = facade.get_all_users()
        return [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            } for user in users
        ], 200

@api.route('/update/<user_id>')

class UserUpdateResource(Resource):
    @jwt_required()
    @api.expect(update_user_model, validate=True)
    @api.response(200, 'User updated successfully')
    @api.response(401, 'Unauthorized action')
    @api.response(404, 'User not found')
    def put(self, user_id):

        """updating user details (email and password cannot be modified)"""

        current_user_id = get_jwt_identity()
        if current_user_id != user_id:
            return {'error': 'Unauthorized action.'}, 401

        user_data = api.payload

        if 'email' in user_data or 'password' in user_data:
            return {'error': 'You cannot modify email or password.'}, 400

        updated_user = facade.update_user(user_id, user_data)
        if not updated_user:
            return {'error': 'User not found'}, 404

        return {
            'message': 'User updated successfully',
            'user': {
                'id': updated_user.id,
                'first_name': updated_user.first_name,
                'last_name': updated_user.last_name,
                'email': updated_user.email
            }
        }, 200
