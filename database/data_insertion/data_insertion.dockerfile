# Use an official Python runtime as the base image
FROM python:3.11-slim

ARG KAGGLE_USR
ARG KAGGLE_TOKEN

# Set the working directory in the container
WORKDIR /usr/src/app

# Install wget and unzip
RUN apt-get update && \
    apt-get install -y wget unzip && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy only the Poetry lock file and pyproject.toml first to leverage Docker caching
#COPY ./database/data_insertion/pyproject.toml ./
COPY pyproject.toml ./

# Install dependencies without virtual environments
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --only database

# Copy the data insertion script and dependecies into the container
COPY ./database/data_insertion/data_insertion.py .
COPY ./database/data_insertion/models.py .
COPY ./database/data_insertion/utils.py .

# Setup kaggle API
RUN mkdir /root/.kaggle/ \
    && echo "{\"username\":\"${KAGGLE_USR}\", \"key\":\"${KAGGLE_TOKEN}\"}" > /root/.kaggle/kaggle.json \
    && chmod 600 /root/.kaggle/kaggle.json


# Use the Kaggle CLI to download the dataset
RUN kaggle datasets download -d austinreese/craigslist-carstrucks-data && \
    unzip craigslist-carstrucks-data.zip  -d ./raw_data && \
    rm craigslist-carstrucks-data.zip

# Command to run the script
CMD ["python", "./data_insertion.py"]
