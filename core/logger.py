# core/logger.py

import logging
import sys

# Logger Configuration
logging.basicConfig(
    level=logging.INFO,  # Default logging level
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Output logs to console
        logging.FileHandler("logs/app.log", mode="a")  # Save logs to a file
    ]
)

# Function to get logger instance
def get_logger(name: str):
    return logging.getLogger(name)
