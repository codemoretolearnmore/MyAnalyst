from celery import Celery
# from app.utils.logger import logger, set_request_id
from ..utils.kafka_producer import produce_event
from ..config import KAFKA_TOPICS, CELERY_BROKER_URL

celery = Celery("tasks", broker=CELERY_BROKER_URL)

@celery.task(bind=True, max_retries=3)
def process_text_to_tables(self, request_id, prompt):
    try:
        # set_request_id(request_id)
        # logger.info(f"Processing text_to_tables for request_id: {request_id}")
        tables_result = {"tables": ["sales", "revenue"], "request_id": request_id}
        produce_event(KAFKA_TOPICS["QUERY_GENERATED"], tables_result)
        # logger.info(f"text_to_tables completed for request_id: {request_id}")
    except Exception as e:
        # logger.error(f"Error in text_to_tables for request_id {request_id}: {str(e)}")
        raise self.retry(exc=e, countdown=5)

@celery.task(bind=True, max_retries=3)
def process_text_to_query(self, request_id, tables):
    try:
        # set_request_id(request_id)
        # logger.info(f"Processing text_to_query for request_id: {request_id}")
        query_result = {"query": "SELECT * FROM sales", "request_id": request_id}
        produce_event(KAFKA_TOPICS["METRICS_FETCHED"], query_result)
        # logger.info(f"text_to_query completed for request_id: {request_id}")
    except Exception as e:
        # logger.error(f"Error in text_to_query for request_id {request_id}: {str(e)}")
        raise self.retry(exc=e, countdown=5)

@celery.task(bind=True, max_retries=3)
def process_query_to_metrics(self, request_id, query):
    try:
        # set_request_id(request_id)
        # logger.info(f"Processing query_to_metrics for request_id: {request_id}")
        metrics_result = {"total_sales": 50000, "request_id": request_id}
        produce_event(KAFKA_TOPICS["INSIGHTS_GENERATED"], metrics_result)
        # logger.info(f"query_to_metrics completed for request_id: {request_id}")
    except Exception as e:
        # logger.error(f"Error in query_to_metrics for request_id {request_id}: {str(e)}")
        raise self.retry(exc=e, countdown=5)

@celery.task(bind=True, max_retries=3)
def process_metrics_to_insights(self, request_id, metrics):
    try:
        # set_request_id(request_id)
        # logger.info(f"Processing metrics_to_insights for request_id: {request_id}")
        insights_result = {"insight": "Sales have increased by 10%", "request_id": request_id}
        produce_event(KAFKA_TOPICS["INSIGHTS_GENERATED"], insights_result)
        # logger.info(f"metrics_to_insights completed for request_id: {request_id}")
    except Exception as e:
        # logger.error(f"Error in metrics_to_insights for request_id {request_id}: {str(e)}")
        raise self.retry(exc=e, countdown=5)