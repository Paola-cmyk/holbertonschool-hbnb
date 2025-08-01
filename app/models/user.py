from app.models.base_model import BaseModel
from app import db, bcrypt

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name[:50]
        self.last_name = last_name[:50]
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    def register(self):
        print(f"User registered: {self.first_name} {self.last_name} ({self.email})")

    def update_profile(self, data):
        self.update(data)

import re

class User:
    def __init__(self, first_name, last_name, email):
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty.")
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format.")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def _is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def hash_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        """Return a safe representation of the user."""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin
        }
