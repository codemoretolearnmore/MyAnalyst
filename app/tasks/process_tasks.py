from celery import Celery
# from app.utils.logger import logger, set_request_id
from ..utils.kafka_producer import produce_event
from ..config import KAFKA_TOPICS, CELERY_BROKER_URL
import json

celery = Celery("tasks", broker=CELERY_BROKER_URL)

@celery.task(bind=True, max_retries=3)
def process_text_to_tables(self, request_id, prompt):
    try:
        print(f"Processing text_to_tables for request_id: {request_id}", flush=True)
        tables_result = {"tables": ["sales", "revenue"], "request_id": request_id}
        produce_event(KAFKA_TOPICS["TABLES_EXTRACTED"], json.dumps(tables_result))
    except Exception as e:
        print(f"❌ Failed text_to_tables for request_id {request_id}: {str(e)}", flush=True)
        raise self.retry(exc=e, countdown=5)

@celery.task(bind=True, max_retries=3)
def process_text_to_query(self, request_id, tables):
    try:
        print(f"Processing text_to_query for request_id: {request_id}", flush=True)
        query_result = {"query": "SELECT * FROM sales", "request_id": request_id}
        produce_event(KAFKA_TOPICS["QUERY_GENERATED"], json.dumps(query_result))
    except Exception as e:
        print(f"❌ Failed text_to_query for request_id {request_id}: {str(e)}", flush=True)
        raise self.retry(exc=e, countdown=5)

@celery.task(bind=True, max_retries=3)
def process_query_to_metrics(self, request_id, query):
    try:
        print(f"Processing query_to_metrics for request_id: {request_id}", flush=True)
        metrics_result = {"metrics": 50000, "request_id": request_id}
        produce_event(KAFKA_TOPICS["METRICS_FETCHED"], json.dumps(metrics_result))
    except Exception as e:
        print(f"❌ Failed query_to_metrics for request_id {request_id}: {str(e)}", flush=True)
        raise self.retry(exc=e, countdown=5)

@celery.task(bind=True, max_retries=3)
def process_metrics_to_insights(self, request_id, metrics):
    try:
        print(f"Processing metrics_to_insights for request_id: {request_id}", flush=True)
        insights_result = {"insight": "Sales have increased by 10%", "request_id": request_id}
        produce_event(KAFKA_TOPICS["INSIGHTS_CREATED"], json.dumps(insights_result))
    except Exception as e:
        print(f"❌ Failed metrics_to_insights for request_id {request_id}: {str(e)}", flush=True)
        raise self.retry(exc=e, countdown=5)
