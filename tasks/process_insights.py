from celery import Celery
from core.db import get_db
from services.insights_service import generate_insights
from services.status_manager import update_status
import logging

celery_app = Celery("tasks", broker="redis://localhost:6379/0")
logger = logging.getLogger("process_insights")

@celery_app.task(bind=True, max_retries=3)
def process_insights(self, request_id: str):
    """
    Generates insights from the calculated metrics.
    """
    db = next(get_db())
    try:
        insights = generate_insights(db, request_id)
        update_status(db, request_id, "INSIGHTS_GENERATION_COMPLETED", insights)
        logger.info(f"Insights generation completed for request_id: {request_id}")
    except Exception as e:
        logger.error(f"Insights generation failed for {request_id}: {str(e)}")
        self.retry(exc=e)
