from loguru import logger

# Configure logger (e.g., format, rotation, etc.)
# This is just a basic setup, you can further customize it based on your needs.
logger.add("app.log", rotation="10 MB")

