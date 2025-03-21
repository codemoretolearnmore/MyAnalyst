from ..tasks.process_tasks import process_text_to_tables, process_text_to_query, process_query_to_metrics, process_metrics_to_insights

def start_workflow(request_id, prompt):
    process_text_to_tables.apply_async(args=[request_id, prompt])
    return {"status": "Workflow started", "request_id": request_id}