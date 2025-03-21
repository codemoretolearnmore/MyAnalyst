# from app.utils.logger import logger, set_request_id

def process_metrics_to_insights(request_id, metrics):
    # set_request_id(request_id)
    # logger.info(f"Processing metrics_to_insights for request_id: {request_id}")
    
    insights = {"insight": "Sales performance is strong in Q1", "request_id": request_id}
    
    # logger.info(f"Final insights generated for request_id: {request_id}: {insights}")
    return insights