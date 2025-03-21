# from app.utils.logger import logger, set_request_id
from app.utils.kafka_producer import produce_event
from ..config import KAFKA_TOPICS

def process_query_to_metrics(request_id, query):
    # set_request_id(request_id)
    # logger.info(f"Processing query_to_metrics for request_id: {request_id}")
    
    metrics = {"total_sales": 50000, "average_revenue": 12000, "request_id": request_id}
    
    produce_event(KAFKA_TOPICS["INSIGHTS_CREATED"], metrics)
    # logger.info(f"query_to_metrics completed for request_id: {request_id}")