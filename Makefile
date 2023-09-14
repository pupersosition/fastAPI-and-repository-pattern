SHELL := /bin/bash

# Variables
ENV_VARS = PYTHONPATH=./app/api:./app/repositories:./app

# Default target to set up the environment
setup:
	poetry config virtualenvs.in-project true
	poetry install
	poetry shell

# Target to run tests
pytest:
	$(ENV_VARS) pytest tests/*


# Target to clean virtual environment
clean:
	rm -rf .venv

# Combine setup and test
test: setup pytest clean