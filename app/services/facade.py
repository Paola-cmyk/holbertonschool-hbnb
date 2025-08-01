from datetime import datetime

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

 # ------------------- user ------------------- #
class HBnBFacade:
    def create_user(self, data):
        required_fields = ['first_name', 'last_name', 'email']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"{field.replace('_', ' ').capitalize()} is required.")
        
        User = get_user_model()
        if User.get_by_email(data['email']):
            raise ValueError("User with this email already exists.")

        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data.get('password')
        )
        user.save()
        return user

    def get_all_users(self):
        User = get_user_model()
        return User.all()

    def get_user(self, user_id):
        User = get_user_model()
        return User.get_by_id(user_id)

    def update_user(self, user_id, data):
        User = get_user_model()
        user = User.get_by_id(user_id)
        if not user:
            return None
        
        for key in ['first_name', 'last_name', 'email']:
            if key in data and data[key]:
                if key == 'email' and User.get_by_email(data[key]) and User.get_by_email(data[key]).id != user_id:
                    raise ValueError("Email already in use.")
                setattr(user, key, data[key].lower() if key == 'email' else data[key])
        
        user.updated_at = datetime.utcnow()
        user.save()
        return user

    # ------------------- places ------------------- #

    def create_place(self, data):
        User = get_user_model()
        Place = get_place_model()

        owner = User.get_by_id(data['owner_id'])
        if not owner:
            raise ValueError("Owner not found.")

        place = Place(
            title=data['title'],
            description=data.get('description', ''),
            price=data['price'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            owner_id=data['owner_id'],
            amenities=data['amenities']
        )
        place.save()
        return place

    def get_all_places(self):
        Place = get_place_model()
        return [place.to_dict() for place in Place.all()]

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
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner_id": place.owner_id,
            "owner": owner.to_dict() if owner else None,
            "amenities": [a.to_dict() for a in amenities if a],
            "reviews": [r.to_dict() for r in reviews]
        }

    def update_place(self, place_id, data):
        Place = get_place_model()
        place = Place.get_by_id(place_id)
        if not place:
            return None

        for key, value in data.items():
            if hasattr(place, key):
                setattr(place, key, value)

        place.save()
        return place
    
   # --------------- amenity ------------------- #

    def create_amenity(self, data):
        if 'name' not in data or not data['name']:
            raise ValueError("Amenity name is required.")
        Amenity = get_amenity_model()
        amenity = Amenity(name=data['name'])
        amenity.save()
        return amenity

    def get_all_amenities(self):
        Amenity = get_amenity_model()
        return Amenity.all()

    def get_amenity(self, amenity_id):
        Amenity = get_amenity_model()
        return Amenity.get_by_id(amenity_id)

    def update_amenity(self, amenity_id, data):
        Amenity = get_amenity_model()
        amenity = Amenity.get_by_id(amenity_id)
        if not amenity:
            return None
        if 'name' in data and data['name']:
            amenity.name = data['name']
            amenity.updated_at = datetime.utcnow()
            amenity.save()
        return amenity


class HBnBFacade:
    # ------------------- reviews ------------------- #
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
