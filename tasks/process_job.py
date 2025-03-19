from celery import Celery
from core.db import get_db
from services.job_service import process_job
import logging

celery_app = Celery("tasks", broker="redis://localhost:6379/0")
logger = logging.getLogger("process_job")

@celery_app.task
def execute_job(request_id: str, prompt: str):
    """
    Initializes job processing for a given request.
    """
    try:
        db = next(get_db())
        logger.info(f"Starting job processing for request_id: {request_id}")
        process_job(db, request_id, prompt)
        logger.info(f"Job {request_id} processing initiated successfully.")
    except Exception as e:
        logger.error(f"Job {request_id} failed to start: {str(e)}")
