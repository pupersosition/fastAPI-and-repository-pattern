# used_cars_api

A test case for a data serving Fast API api. 
Data Source: Kaggle's **austinreese/craigslist-carstrucks-data**

## Development Requirements

- Python3.11.0
- Pip
- Poetry (Python Package Manager)


## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

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


## GCP
Deploying inference service to Cloud Run

### Authenticate

1. Install `gcloud` cli
2. `gcloud auth login`
3. `gcloud config set project <PROJECT_ID>`

### Enable APIs

1. Cloud Run API
2. Cloud Build API
3. IAM API

### Deploy to Cloud Run

1. Run `gcp-deploy.sh`

### Clean up

1. Delete Cloud Run
2. Delete Docker image in GCR

## AWS
Deploying inference service to AWS Lambda

### Authenticate

1. Install `awscli` and `sam-cli`
2. `aws configure`

### Deploy to Lambda

1. Run `sam build`
2. Run `sam deploy --guiChange this portion for other types of models
## Add the correct type hinting when completed

`aws cloudformation delete-stack --stack-name <STACK_NAME_ON_CREATION>`


Made by https://github.com/arthurhenrique/cookiecutter-fastapi/graphs/contributors with ❤️
