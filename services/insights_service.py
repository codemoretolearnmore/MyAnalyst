from core.db import get_db
from services.status_manager import update_status
from datetime import datetime

def generate_insights(request_id: str, metrics: dict):
    """Generates AI-driven insights from the calculated metrics."""
    db = next(get_db())
    update_status(request_id, "insights_service", "RUNNING")

    try:
        # Simulated insight generation logic
        insights = f"Sales are stable, with an average order value of ${metrics['avg_order_value']}."

        result = {"insights": insights, "generated_at": datetime.utcnow()}
        db.insights.insert_one({"request_id": request_id, **result})

        update_status(request_id, "insights_service", "COMPLETED")
        return result

    except Exception as e:
        update_status(request_id, "insights_service", "FAILED", str(e))
        raise e
