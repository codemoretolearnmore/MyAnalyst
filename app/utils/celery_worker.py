from celery import Celery
from ..config import CELERY_BACKEND_URL, CELERY_BROKER_URL

celery = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL,
    include=["app.services.workflow"]
)

celery.conf.update(task_serializer="json")
