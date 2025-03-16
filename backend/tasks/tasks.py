from .workers import celery_app

@celery_app.task
def background_analysis(query_id):
    # Runs analysis on new data in the background.
    pass
