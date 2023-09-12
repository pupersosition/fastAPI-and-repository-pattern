from loguru import logger

# Log format configuration
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

# Ensure logs directory exists
import os
if not os.path.exists('logs'):
    os.makedirs('logs')

# Loguru logger configuration
logger.remove()
logger.add(
    "logs/app.log",       # Log file path
    rotation="100 MB",    # Rotate the log file when it reaches 100 MB
    retention="7 days",   # Keep logs for a maximum of 7 days
    format=log_format,   # Use the defined log format
    level="INFO",        # Capture logs from INFO level and above
    backtrace=True,      # Provide extended traceback info on exceptions
    diagnose=True,       # Provide diagnostic info on exceptions
)

# This will make the logger available as `logger` whenever the module is imported
__all__ = ['logger']
