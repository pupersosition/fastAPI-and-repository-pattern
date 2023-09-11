FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Install poetry
RUN pip install --no-cache-dir poetry

# Switch working directory
WORKDIR /

# Copy only dependencies definition
COPY pyproject.toml /

# Install runtime deps using poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy application code to the container
COPY . /

WORKDIR /app
ENV PYTHONPATH=./api

# Run the uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]