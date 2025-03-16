import logging
from fastapi import Request
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

async def log_request_response(request: Request, call_next):
    """
    Middleware to log API requests and responses.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.2f}s")
    return response
