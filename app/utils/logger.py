import logging
import contextvars

# Create a context variable for request_id
request_id_var = contextvars.ContextVar("request_id", default="N/A")

# Configure logging
logging.basicConfig(
    filename="app/app.log",
    level=logging.INFO,
    format="{asctime} - {levelname} - [Request ID: {request_id}] - {message}",
    style="{"
)


class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get()  # Ensure request_id exists
        return True

logger = logging.getLogger("GenAI")
logger.addFilter(RequestIDFilter())

def set_request_id(request_id: str):
    request_id_var.set(request_id)
