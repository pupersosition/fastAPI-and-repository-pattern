# 🚗 Used Car Data API with FastAPI

This repository contains a FastAPI application designed to serve data about used cars sourced from Kaggle. It provides an intuitive API to query, filter, and access detailed records of used cars. Whether you're a data enthusiast, researcher, or developer, this API is designed to help you harness the power of used car data at your fingertips.

## 🔥 Features

- Rich Data Set: Details about make, model, price, mileage, and more.
- Fast & Efficient: Powered by FastAPI for high-speed performance.
- Interactive Docs: Explore the API using FastAPI's built-in Swagger UI.


## 🚀 Quick Start

### Prerequisites
Python 3.7+
Pip
### Installation & Setup
Clone the repository:
bash
Copy code
git clone https://github.com/[YourGitHubUsername]/used-car-data-api.git
cd used-car-data-api
Install the requirements:
bash
Copy code
pip install -r requirements.txt
Run the FastAPI application:
bash
Copy code
uvicorn main:app --reload
Access the API documentation at http://127.0.0.1:8000/docs.

## 🌐 Endpoints

/cars: Get a list of all used cars.
/cars/{id}: Get detailed information about a specific car by its ID.
... [Add more endpoints or details as required]
## 📜 Data Source

The data utilized in this application is sourced from Kaggle. Special thanks to [Link to Kaggle Dataset Author/Source] for making this data publicly available.

Testing

Instructions or scripts related to testing the API.

Contributing

We welcome contributions! Please see the CONTRIBUTING.md for details.

License

This project is licensed under the MIT License. See LICENSE for more details.

Acknowledgements

FastAPI: For their amazing asynchronous web framework.
Kaggle: For hosting the dataset and fostering a community around data.
... [Add any other acknowledgements or tools/libraries you've used]

## 🧪 Testing

[Provide instructions or mention testing utilities/methods you've used]

## 📄 License

MIT License

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
    │   │   └── logging.py             - Logger.
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
    │   │   └── manufacturer.py        - Pydantic model for manufacturers.
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


## 💖 Acknowledgements

- FastAPI
- Kaggle
