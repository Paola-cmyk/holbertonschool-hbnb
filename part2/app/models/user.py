from app.models.base_model import BaseModel

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

