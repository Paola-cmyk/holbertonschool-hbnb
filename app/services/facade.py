def get_user_model():
    from app.models.user import User
    return User

def get_place_model():
    from app.models.place import Place
    return Place

def get_amenity_model():
    from app.models.amenity import Amenity
    return Amenity

def get_review_model():
    from app.models.review import Review
    return Review


class HBnBFacade:
    def create_review(self, review_data):
        User = get_user_model()
        Place = get_place_model()
        Review = get_review_model()

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
        Review = get_review_model()
        return Review.get_by_id(review_id)

    def get_all_reviews(self):
        Review = get_review_model()
        return Review.all()

    def get_reviews_by_place(self, place_id):
        Place = get_place_model()
        Review = get_review_model()
        place = Place.get_by_id(place_id)
        if not place:
            return None
        return Review.find_by_place_id(place_id)

    def update_review(self, review_id, review_data):
        Review = get_review_model()
        review = Review.get_by_id(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            if hasattr(review, key):
                setattr(review, key, value)
        review.save()
        return review

    def delete_review(self, review_id):
        Review = get_review_model()
        review = Review.get_by_id(review_id)
        if not review:
            return False
        review.delete()
        return True

    def get_place(self, place_id):
        Place = get_place_model()
        User = get_user_model()
        Amenity = get_amenity_model()
        Review = get_review_model()

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
