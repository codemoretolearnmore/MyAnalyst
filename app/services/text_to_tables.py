# from app.utils.logger import logger, set_request_id
from ..utils.kafka_producer import produce_event
from ..config import KAFKA_TOPICS

def process_text_to_tables(request_id, prompt):
    # set_request_id(request_id)
    # logger.info(f"Processing text_to_tables for request_id: {request_id}")
    
    tables_result = {"tables": ["sales", "revenue"], "request_id": request_id}
    
    produce_event(KAFKA_TOPICS["QUERY_GENERATED"], tables_result)
    # logger.info(f"text_to_tables completed for request_id: {request_id}")