# core/task_queue.py

from celery import Celery
from config import settings

# Initialize Celery
celery_app = Celery(
    "task_queue",
    broker=settings.REDIS_BROKER_URL,
    backend=settings.REDIS_BROKER_URL
)

# Celery configurations
celery_app.conf.update(
    task_routes={
        "tasks.process_job.*": {"queue": "job_queue"},
        "tasks.process_insights.*": {"queue": "insight_queue"}
    },
    task_acks_late=True,
    task_reject_on_worker_lost=True
)
