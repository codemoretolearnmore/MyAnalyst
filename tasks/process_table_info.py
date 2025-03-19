from celery import Celery
from core.db import get_db
from services.table_info_service import identify_tables
from services.status_manager import update_status
import logging

celery_app = Celery("tasks", broker="redis://localhost:6379/0")
logger = logging.getLogger("process_table_info")

@celery_app.task(bind=True, max_retries=3)
def process_table_info(self, request_id: str, prompt: str):
    """
    Identifies relevant tables based on the user prompt.
    """
    db = next(get_db())
    try:
        tables = identify_tables(db, request_id, prompt)
        update_status(db, request_id, "TABLE_IDENTIFICATION_COMPLETED", tables)
        logger.info(f"Table identification completed for request_id: {request_id}")
    except Exception as e:
        logger.error(f"Table identification failed for {request_id}: {str(e)}")
        self.retry(exc=e)
