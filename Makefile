SHELL := /bin/bash

# Variables
ENV_VARS = PYTHONPATH=./app/api:./app/repositories:./app DB_USER=postgres POSTGRES_PASSWORD=yourpassword DB_HOST=db DB_NAME=postgres

# Default target to set up the environment
setup:
	poetry config virtualenvs.in-project true
	poetry install

# Target to run tests
pytest:
	$(ENV_VARS) poetry run pytest tests/*


# Target to clean virtual environment
clean:
	rm -rf .venv

# Combine setup and test
test: setup pytest clean