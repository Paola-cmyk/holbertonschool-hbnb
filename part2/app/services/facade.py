from app.models import Place, User, Amenity, Review

class HBnBFacade:

    # -- REVIEW LOGIC --

    def create_review(self, review_data):
        try:
            user = User.get_by_id(review_data['user_id'])
            place = Place.get_by_id(review_data['place_id'])
            if not user or not place:
                raise ValueError("User or Place not found.")
            review = Review(**review_data)
            review.save()
            return review
        except ValueError as e:
            raise ValueError(str(e))

    def get_review(self, review_id):
        return Review.get_by_id(review_id)

    def get_all_reviews(self):
        return Review.all()

    def get_reviews_by_place(self, place_id):
        place = Place.get_by_id(place_id)
        if not place:
            return None
        return Review.find_by_place_id(place_id)

    def update_review(self, review_id, review_data):
        review = Review.get_by_id(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            if hasattr(review, key):
                setattr(review, key, value)
        review.save()
        return review

    def delete_review(self, review_id):
        review = Review.get_by_id(review_id)
        if not review:
            return False
        review.delete()
        return True

def get_place(self, place_id):
    place = Place.get_by_id(place_id)
    if not place:
        return None

    owner = User.get_by_id(place.owner_id)
    amenities = [Amenity.get_by_id(aid) for aid in place.amenities]
    reviews = Review.find_by_place_id(place.id)

    return {
        "id": place.id,
        "title": place.title,
        "description": place.description,
        "latitude": place.latitude,
        "longitude": place.longitude,
        "owner": {
            "id": owner.id,
            "first_name": owner.first_name,
            "last_name": owner.last_name,
            "email": owner.email
        },
        "amenities": [{"id": a.id, "name": a.name} for a in amenities if a],
        "reviews": [{
            "id": r.id,
            "text": r.text,
            "rating": r.rating,
            "user_id": r.user_id
        } for r in reviews]
    }
