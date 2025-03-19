from core.db import get_db
from services.status_manager import update_status
from datetime import datetime

def generate_query(request_id: str, tables: list, prompt: str):
    """Generates an SQL query based on the identified tables and prompt."""
    db = next(get_db())
    update_status(request_id, "query_service", "RUNNING")

    try:
        # Simulated SQL query generation
        query = f"SELECT * FROM {', '.join(tables)} WHERE condition_based_on_prompt"

        result = {"query": query, "generated_at": datetime.utcnow()}
        db.queries.insert_one({"request_id": request_id, **result})

        update_status(request_id, "query_service", "COMPLETED")
        return result

    except Exception as e:
        update_status(request_id, "query_service", "FAILED", str(e))
        raise e
