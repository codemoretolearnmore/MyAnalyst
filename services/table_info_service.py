from core.db import get_db
from services.status_manager import update_status
from datetime import datetime

def identify_tables(request_id: str, prompt: str):
    """Extracts relevant tables based on user prompt."""
    db = next(get_db())
    update_status(request_id, "table_info_service", "RUNNING")

    try:
        # Simulated logic for identifying tables
        tables = ["users", "transactions"]  # Example
        result = {"tables": tables, "identified_at": datetime.utcnow()}
        
        db.table_info.insert_one({"request_id": request_id, **result})
        update_status(request_id, "table_info_service", "COMPLETED")
        return result

    except Exception as e:
        update_status(request_id, "table_info_service", "FAILED", str(e))
        raise e
