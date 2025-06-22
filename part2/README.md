# HBnB Project – Part 2: Business Logic & API Implementation

Welcome to Part 2 of the HBnB project! In this part of the HBnB Project, begins the implementation phase of the application based on the design developed in the previous part. We are turning our design into working code by building out the core functionality of the app with the help of  **Flask** and **flask-restx**. 

---

## Project Structure Overview

Organizing the app with clear separation between layers for maintainability and scalability:

```

hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```
---

## Business Logic Highlights

Implemented the key entities that drive the app:

- **User** – someone using the platform
- **Place** – a property listed by a user
- **Review** – feedback on a place
- **Amenity** – services/features offered at a place


---

## API Endpoints

All API endpoints are built with **Flask** and **flask-restx**, following REST principles.

Example endpoints include:

- `/api/users/` – List or create users
- `/api/places/` – Manage places
- `/api/reviews/` – Manage reviews
- `/api/amenities/` – Manage amenities

---

## How to Test

You can test endpoints using tools like:

- **Postman** – import your routes and test easily
- **cURL** – for quick command-line tests

Example:
```bash
curl -X GET http://localhost:5000/api/places/
```

