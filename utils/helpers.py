import time
import logging
from datetime import datetime

logger = logging.getLogger("helpers")

def retry(func, retries=3, delay=2, *args, **kwargs):
    """Retries a function if it fails."""
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
            time.sleep(delay)
    logger.error("Max retries reached. Function execution failed.")
    return None

def get_current_timestamp():
    """Returns the current timestamp in ISO format."""
    return datetime.utcnow().isoformat()
