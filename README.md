# holbertonschool-hbnb: The blueprint

 **Project overview**: HBnB Evolution is a web application inspired by AirBnB, built to handle user sign-ups, property listings, user reviews, and amenity management. This document acts as a detailed technical guide to help during all stages of development. It outlines the system’s structure and design, ensuring everything stays consistent and easy to maintain as the project grows.

 This document focuses on the following key areas:

**System Architecture**: A high-level look at how the application is organized, including a breakdown of the layered architecture and the use of the Facade design pattern.

**Core Business Logic**: Class diagrams that represent the main entities in the system—User, Place, Review, and Amenity—and how they interact with each other.

**API Workflow**: Sequence diagrams that walk through the main API processes like user registration, creating a place, submitting a review, and retrieving a list of available places.

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

	# Sequence Diagrams for API Calls

<a href="https://github.com/Paola-cmyk/holbertonschool-hbnb/blob/main/part1/user_registration.mmd" target="_blank">**Diagram**</a>


**User Registration**: 

**Purpose**: To allow a new user to sign up by providing personal details. The system validates and stores the user data securely.




**Explanatory notes**: 



- **Flow**

    i. User → API: The user submits a ```POST /register``` request with their registration details.

    ii. API → UserService: The API delegates to the ```UserService``` to validate the input.

    iii. UserService → UserModel: Once validated, it calls the model to create a user object.

    iv. UserModel → Database: The model persists the new user record into the database.

    v. Database → UserModel → UserService → API: The created user object is passed back up the chain.

    vi. API → User: The API returns a success response along with the user info.


