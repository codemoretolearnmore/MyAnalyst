from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("error_handler")

async def custom_exception_handler(request: Request, exc: Exception):
    """Handles unexpected errors and returns a structured JSON response."""
    logger.error(f"Unexpected error: {str(exc)} - Path: {request.url.path}")
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred."},
    )
