# holbertonschool-hbnb: The blueprint

 **Project overview**: HBnB Evolution is a web application inspired by AirBnB, built to handle user sign-ups, property listings, user reviews, etc. This document acts as a detailed technical guide to help during all stages of development.
 This focuses on the following areas:

**System Architecture**: A high-level look at how the application is organized.

**Core Business Logic**: Class diagrams that represent the main entities in the system User.

**API Workflow**: Sequence diagrams that walk through the main API processes.

# High-Level Package Diagram

<a href="https://github.com/Paola-cmyk/holbertonschool-hbnb/blob/main/part1/high_lvl_package.md" target="_blank">**Diagram**</a>

``` mermaid 
classDiagram
direction TB
    class PresentationLayer {
	    +ServiceAPI
	    +UserAPI
	    +handleRequest
    }
    class BusinessLogicLayer {
	    +User
	    +Place
	    +Review
	    +Amenity
	    +ProcessRequest()
    }
    class PersistenceLayer {
	    +Database acess
	    +PlaceRepository
	    +excecute()
    }

    PresentationLayer --> BusinessLogicLayer : Facade Pattern
    BusinessLogicLayer --> PersistenceLayer : Database Operations
```


# Detailed Class Diagram for Business Logic Layer

<a href= "https://github.com/Paola-cmyk/holbertonschool-hbnb/blob/main/part1/business_logic_layer.mmd" target="_blank">**Diagram**</a>

**1. User**:
    
- Represents a person using the app.

- Contains information such as name, email, and password.

- Can register, log in, update their profile, and log out.

**2. Place**:

- Represents a property or listing.

- Has details such as like title, description, price, and location.

**3. Review**:
- Feedback or rating left by a user about a place.

- Contains a comment and a rating score

**4. Amenity**:
- Features or services a place offers, like Wi-Fi or parking.

- Has a name and description




---
# Sequence Diagrams for API Calls
<a href= "https://github.com/Paola-cmyk/holbertonschool-hbnb/blob/main/part1/user_registration.mmd" target="_blank">**1. User Registration diagram**</a>

**Flow**: 

i. The user sends their info to the website/app.

ii. The API receives the info and sends it to a service that checks if everything is valid.

iii. The service tells the system to create a new user.

iv. The system stores the user in the database.

v. After saving, it sends a confirmation back.

vi. The user is told their account was created successfully.

<a href= "https://github.com/Paola-cmyk/holbertonschool-hbnb/blob/main/part1/place_creation.mmd" target="_blank">**2. Place creation diagram**</a>

**Flow**:

i. The host submits details about the place (location, price, etc.).

ii. The API sends the details to a service that checks if all info is okay.

iii. The service creates a place listing.

iv. The listing is saved in the database.

v. The system confirms it saved the listing.

vi. The host sees a success message with the new place info.

<a href= "https://github.com/Paola-cmyk/holbertonschool-hbnb/blob/main/part1/review_submission.mmd" target="_blank">**3. Review submission diagram**</a>

i. The user writes a review and submits it.

ii. The API sends the review to a service to check if it’s valid.

iii. If valid, the review is created.

iv. The review is saved in the database.

v. A confirmation is sent back.

vi. The user sees that their review was posted successfully.

<a href= "https://github.com/Paola-cmyk/holbertonschool-hbnb/blob/main/part1/fetching_list.mmd" target="_blank">**4. Fetching a list of places diagram**</a>

i. The user sends a search request with filters like location and guest number.

ii. The API sends these filters to a service.

iii. The service builds a search query.

iv. The system looks in the database for places that match the filters.

v. A list of matching places is sent back.

vi. The user sees the list of places they can book.
