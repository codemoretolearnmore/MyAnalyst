from celery import Celery
from ..config import CELERY_BACKEND_URL, CELERY_BROKER_URL

celery = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL,
    include=["app.services.workflow"]
)

# Correct way to set heartbeat interval
celery.conf.update(
    task_serializer="json",
    worker_heartbeat=300  # Set heartbeat every 5 minutes
)
celery.conf.broker_use_ssl = {"ssl_cert_reqs": "CERT_REQUIRED"}