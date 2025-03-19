from core.db import get_db
from datetime import datetime

def update_status(request_id: str, service: str, status: str, error_message: str = None):
    """Logs status updates for each microservice in the request pipeline."""
    db = next(get_db())
    status_entry = {
        "request_id": request_id,
        "service": service,
        "status": status,
        "updatedAt": datetime.utcnow(),
        "error_message": error_message,
    }
    db.status_logs.insert_one(status_entry)
