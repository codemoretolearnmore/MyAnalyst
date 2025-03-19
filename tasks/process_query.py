from celery import Celery
from core.db import get_db
from services.query_service import generate_query
from services.status_manager import update_status
import logging

celery_app = Celery("tasks", broker="redis://localhost:6379/0")
logger = logging.getLogger("process_query")

@celery_app.task(bind=True, max_retries=3)
def process_query(self, request_id: str):
    """
    Generates an SQL query using the identified tables.
    """
    db = next(get_db())
    try:
        query = generate_query(db, request_id)
        update_status(db, request_id, "QUERY_GENERATION_COMPLETED", query)
        logger.info(f"Query generation completed for request_id: {request_id}")
    except Exception as e:
        logger.error(f"Query generation failed for {request_id}: {str(e)}")
        self.retry(exc=e)
