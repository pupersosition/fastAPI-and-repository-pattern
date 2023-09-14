# 🚗 Used Car Data API with FastAPI

This repository contains a FastAPI application designed to serve data about used cars sourced from Kaggle. It provides an intuitive API to query, filter, and access detailed records of used cars. Whether you're a data enthusiast, researcher, or developer, this API is designed to help you harness the power of used car data at your fingertips.

--- 
## 🔥 Features

- Rich Data Set: Details about make, model, price, mileage, and more.
- Fast & Efficient: Powered by FastAPI for high-speed performance.
- Interactive Docs: Explore the API using FastAPI's built-in Swagger UI.

--- 
### Prerequisites
- Python 3.11
- poetry
- docker

--- 
## 🚀 Quick Start

To run this application localy you would need to obtain a Kaggle API token as during the db initialization phase the data
is pulled using Kaggle API.

Put your Kaggle user name and token in the `.env` file in the root of the project.
Example of the environmental vairables file is provided in `.env.example`.

Once you created this file and provided Kaggle token, you can execute:

```bash
docker compose up
```

This command will download the data from Kaggle, setup the Postgres database, populate it with data and start the API
to serve the data.

Access the API Swagger documentation at http://localhost:8000/docs.


--- 

## 🌐 Endpoints

### Car API

#### 1. Add a New Car

- **URL:** `/`
- **Method:** `POST`
- **Description:** Add a new car to the database.
- **Data Parameters:** Provide car details in the request body.

#### 2. Retrieve a Car's Details

- **URL:** `/{car_id}`
- **Method:** `GET`
- **Description:** Retrieve details of a specific car using its ID.
- **Notes:** Limited to 5 requests per minute.

#### 3. List All Cars

- **URL:** `/`
- **Method:** `GET`
- **Description:** Get a list of all cars. Supports pagination.
- **Query Parameters:**
    - `skip` - Number of records to skip (optional, default is 0).
    - `limit` - Number of records to retrieve (optional, default is 10).

#### 4. Update Car Details

- **URL:** `/{car_id}`
- **Method:** `PATCH`
- **Description:** Update the details of a specific car using its ID.
- **Data Parameters:** Provide updated car details in the request body.

#### 5. Remove a Car

- **URL:** `/{car_id}`
- **Method:** `DELETE`
- **Description:** Delete a specific car using its ID.


### Manufacturer API

#### 1. Add a New Manufacturer

- **URL:** `/`
- **Method:** `POST`
- **Description:** Add a new car manufacturer to the database.
- **Data Parameters:** Provide manufacturer details in the request body.

#### 2. Retrieve a Manufacturer's Details

- **URL:** `/{manufacturer_id}`
- **Method:** `GET`
- **Description:** Retrieve details of a specific manufacturer using its ID.

#### 3. List All Manufacturers

- **URL:** `/`
- **Method:** `GET`
- **Description:** Get a list of all manufacturers. Supports pagination.
- **Query Parameters:**
    - `skip` - Number of records to skip (optional, default is 0).
    - `limit` - Number of records to retrieve (optional, default is 10).

#### 4. Update Manufacturer Details

- **URL:** `/{manufacturer_id}`
- **Method:** `PATCH`
- **Description:** Update the details of a specific manufacturer using its ID.
- **Data Parameters:** Provide updated manufacturer details in the request body.

#### 5. Remove a Manufacturer

- **URL:** `/{manufacturer_id}`
- **Method:** `DELETE`
- **Description:** Delete a specific manufacturer using its ID.



--- 

## 📜 Data Source

The data utilized in this application is sourced from Kaggle. Special thanks to 
[austinreese/craigslist-carstrucks-data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)
for making this data publicly available.


--- 

## 🧪 Testing

To run tests in the root of the repository you can execute

```bash
make test
```

--- 
## 📄 License

MIT License

--- 
## 📂 Project Structure

Application parts are:

    .
    ├── app
    │   | # Main FAST API
    │   ├── api             - Contains all the route definitions.
    │   │   └── routes
    │   │       ├── cars.py          - Routes for cars.
    │   │       └── manufacturer.py  - Routes for manufacturers.
    │   ├── core            - Core functionalities like exceptions, handlers, and logging.
    │   │   ├── errors.py              - Custom exceptions.
    │   │   ├── exception_handlers.py  - FAST API exception handlers.
    │   │   ├── logging.py             - Logger.
    │   │   └── rate_limit.py          - Rate limit demonstration
    │   ├── db              - Everything database-related.
    │   │   ├── base        - Handles database connection.
    │   │   └── session     - Deals with the database session.
    │   ├── docker          - Docker configurations.
    │   │   └── api.dockerfile - Dockerfile for the API.
    │   ├── models          - ORM SQLAlchemy models.
    │   │   ├── cars.py                - ORM model for cars.
    │   │   └── manufacturer.py        - ORM model for manufacturers.
    │   ├── repositories    - Implements the repository design pattern for db interactions.
    │   │   ├── base.py                - Base repository.
    │   │   └── sqlalchemy_repository.py - Repository for SQLAlchemy.
    │   ├── schemas         - Pydantic models.
    │   │   ├── car.py                 - Pydantic model for cars.
    │   │   ├── manufacturer.py        - Pydantic model for manufacturers.
    │   │   └── pagination.py          - Pydantic model for pagination
    │   ├── services        - Business logic and CRUD operations.
    │   │   ├── cars.py                - Service for cars.
    │   │   └── manufacturers.py       - Service for manufacturers.
    │   └── main.py         - Main application script.
    |
    ├── database
    │   | # Database setup and initial data insertion.
    │   └── data-insertion
    │       ├── data_insertion.dockerfile  - Dockerfile for data insertion.
    │       ├── data_insertion.py          - Script to insert initial data.
    │       ├── models.py                  - ORM models.
    │       └── utils.py                   - Utilities for data insertion.
    |
    └── tests               - Tests for the application.
        ├── test_sqlalchemy_car_repository.py           - testing the methods provided by the car repository
        └── test_sqlalchemy_manufacturer_repository.py  - testing the methods provided by the manufacturer repository
--- 
## 💖 Acknowledgements

- FastAPI
- Kaggle

## 🚧 Further Improvements

This project is just a demonstration. The proper production ready API would also need following components to be 
implemented:

- More data manipulation functionality, some business logic going to `app/services`.
- More tests to cover more cases and application components
- Scaling and deployment. This is a separate big task to plan for proper deployment and architecture allowing for 
appropriate scaling and load handling (Kubernetes, AWS, Google Cloud, Azure, CloudFoundry, etc.)
- CI/CD for deployment and releases
- Caching. Frequent requests can be cached. Redis can be a solution
- Monitoring & Logging. In addition to the simple logging mechanism provided here, proper monitoring should be configured
For example, ELK Stack (elasticsearch, Logstash, Kibana) for logging, Prometheus for monitoring
- Security. Setup HTTPS, rate limiting, authentication and authorization. This doesn't make sense for local demonstration,
however it is an important point to implement in production system
