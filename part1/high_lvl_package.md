# High- Level Package Diagram

1. Presentation Layer

    - **Purpose**: The presentation layer serves as the interface between the user  and the core application. It is responsible for handling incoming service or user requests and delegating them appropriately.
    - **Components**: 
    - ```+serviceAPI``` and ```+UserAPI```: Represent public-facing interfaces that expose application functionality.
    - ```+handleRequest``` Manages incoming requests and forwards them to the business logic layer for processing.

2. Business Logic Layer

    - **Purpose**: This layer encapsulates the core functionality and rules of the application. It processes data, enforces business rules, and coordinates the application's behavior.

    - **Key Components**: Domain Entities: ```+User```, ```+Place```, ```+Review```, ```+Amenity``` — these represent the core data models used within the system.
    - ```+ProcessRequest()```: A method that contains the primary logic for processing application-specific workflows and operations.

3. Persistance Layer
    
    - **Purpose**: The Persistence Layer abstracts all data storage and retrieval operations. It manages interactions with the underlying database.

    - **Key Components**: ```+Database access```: Handles connections and communication with the database system.

    - ```+PlaceRepository```: A data access class responsible for managing Place entity persistence and queries.

    - ```+execute()```: Executes data-related operations, such as CRUD actions or custom queries.

    # Inter-layer relationships

- ```PresentationLayer --> BusinessLogicLayer : Facade Pattern```
This indicates that the Presentation Layer interacts with the Business Logic Layer through a Facade Pattern. The facade provides a simplified and unified interface to a more complex subsystem, thus promoting encapsulation and reducing coupling between layers.

- ```BusinessLogicLayer --> PersistenceLayer : Database Operations```
The Business Logic Layer relies on the Persistence Layer for executing database operations. This design enables the logic layer to remain independent of specific database implementations, fostering modularity and easier testing.
