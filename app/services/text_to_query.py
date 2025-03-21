# from app.utils.logger import logger, set_request_id
from app.utils.kafka_producer import produce_event
from ..config import KAFKA_TOPICS

def process_text_to_query(request_id, tables):
    # set_request_id(request_id)
    # logger.info(f"Processing text_to_query for request_id: {request_id}")
    
    sql_query = "SELECT * FROM sales WHERE revenue > 10000;"
    query_result = {"query": sql_query, "request_id": request_id}
    
    produce_event(KAFKA_TOPICS["METRICS_FETCHED"], query_result)
    # logger.info(f"text_to_query completed for request_id: {request_id}")