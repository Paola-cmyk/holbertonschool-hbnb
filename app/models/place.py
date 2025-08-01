import uuid
from datetime import datetime
from app import db
from .base_model import BaseModel

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    owner_id = db.Column(db.String(36), nullable=False)

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None, **kwargs):

        if not title:
            raise ValueError("Title cannot be empty.")
        if price < 0:
            raise ValueError("Price must be non-negative.")
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180.")

        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.title = title
        self.description = description or ""
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities or []
        self.created_at = kwargs.get("created_at", datetime.utcnow())
        self.updated_at = kwargs.get("updated_at", datetime.utcnow())

    def save(self):
        print(f"Saving place: {self.title}")

    def delete(self):
        print(f"Deleting place {self.id}")

    @classmethod
    def get_by_id(cls, place_id):
        print(f"Fetching place by ID: {place_id}")
        return None

    @classmethod
    def all(cls):
        return []

    @staticmethod
    def find_by_owner_id(owner_id):
        return []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": self.amenities,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
