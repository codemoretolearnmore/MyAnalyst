from core.db import get_db
from services.status_manager import update_status
from datetime import datetime

def calculate_metrics(request_id: str, query: str):
    """Executes the query and computes relevant metrics."""
    db = next(get_db())
    update_status(request_id, "metrics_service", "RUNNING")

    try:
        # Simulated metric calculation logic
        metrics = {"total_sales": 50000, "avg_order_value": 200}  # Example data

        result = {"metrics": metrics, "calculated_at": datetime.utcnow()}
        db.metrics.insert_one({"request_id": request_id, **result})

        update_status(request_id, "metrics_service", "COMPLETED")
        return result

    except Exception as e:
        update_status(request_id, "metrics_service", "FAILED", str(e))
        raise e
