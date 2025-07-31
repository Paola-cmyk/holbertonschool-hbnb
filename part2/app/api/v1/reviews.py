from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('reviews', description='Review operations')
facade = HBnBFacade()

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
    'user_id': fields.String(required=True, description='User ID'),
    'place_id': fields.String(required=True, description='Place ID')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review created')
    @api.response(400, 'Invalid input')
    def post(self):
        """Create a review"""
        try:
            review = facade.create_review(api.payload)
            return {
                "id": review.id,
                "text": review.text,
                "rating": review.rating,
                "user_id": review.user_id,
                "place_id": review.place_id
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, 'Reviews fetched')
    def get(self):
        """Get all reviews"""
        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating
            } for r in facade.get_all_reviews()
        ], 200

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review found')
    @api.response(404, 'Not found')
    def get(self, review_id):
        """Get a review"""
        r = facade.get_review(review_id)
        if not r:
            return {"error": "Review not found"}, 404
        return {
            "id": r.id,
            "text": r.text,
            "rating": r.rating,
            "user_id": r.user_id,
            "place_id": r.place_id
        }, 200

    @api.expect(review_model)
    @api.response(200, 'Updated')
    @api.response(400, 'Invalid data')
    @api.response(404, 'Not found')
    def put(self, review_id):
        """Update a review"""
        try:
            r = facade.update_review(review_id, api.payload)
            if not r:
                return {"error": "Review not found"}, 404
            return {"message": "Review updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, 'Deleted')
    @api.response(404, 'Not found')
    def delete(self, review_id):
        """Delete a review"""
        success = facade.delete_review(review_id)
        if not success:
            return {"error": "Review not found"}, 404
        return {"message": "Review deleted successfully"}, 200

@api.route('/places/<string:place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'Reviews for place fetched')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a place"""
        reviews = facade.get_reviews_by_place(place_id)
        if reviews is None:
            return {"error": "Place not found"}, 404
        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating
            } for r in reviews
        ], 200
