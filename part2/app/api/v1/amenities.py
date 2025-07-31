from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')
facade = HBnBFacade()

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

response_model = api.inherit('AmenityResponse', amenity_model, {
    'id': fields.String(readOnly=True)
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.marshal_with(response_model, code=201)
    @api.response(400, 'Invalid input data')
    def post(self):

        data = request.json
        try:
            amenity = facade.create_amenity(data)
            return amenity.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))

    @api.marshal_list_with(response_model)
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):

        amenities = facade.get_all_amenities()
        return [a.to_dict() for a in amenities]

@api.route('/<string:amenity_id>')
@api.param('amenity_id', 'The Amenity identifier')
class AmenityResource(Resource):
    @api.marshal_with(response_model)
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found')
        return amenity.to_dict()

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = request.json
        if 'name' not in data:
            api.abort(400, 'Missing required field: name')
        amenity = facade.update_amenity(amenity_id, data)
        if not amenity:
            api.abort(404, 'Amenity not found')
        return {'message': 'Amenity updated successfully'}, 200
