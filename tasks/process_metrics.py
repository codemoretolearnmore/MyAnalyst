from celery import Celery
from core.db import get_db
from services.metrics_service import calculate_metrics
from services.status_manager import update_status
import logging

celery_app = Celery("tasks", broker="redis://localhost:6379/0")
logger = logging.getLogger("process_metrics")

@celery_app.task(bind=True, max_retries=3)
def process_metrics(self, request_id: str):
    """
    Executes SQL query and calculates required metrics.
    """
    db = next(get_db())
    try:
        metrics = calculate_metrics(db, request_id)
        update_status(db, request_id, "METRICS_CALCULATION_COMPLETED", metrics)
        logger.info(f"Metrics calculation completed for request_id: {request_id}")
    except Exception as e:
        logger.error(f"Metrics calculation failed for {request_id}: {str(e)}")
        self.retry(exc=e)
