import uuid
from models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.amenities = {}

    def create_amenity(self, amenity_data):
        if not amenity_data.get('name'):
            raise ValueError("Name is required")
        amenity_id = str(uuid.uuid4())
        amenity = Amenity(id=amenity_id, name=amenity_data['name'])
        self.amenities[amenity_id] = amenity
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenities.get(amenity_id)

    def get_all_amenities(self):
        return list(self.amenities.values())

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenities.get(amenity_id)
        if not amenity:
            return None
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']
        return amenity
