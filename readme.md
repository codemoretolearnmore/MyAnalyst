python -m app.utils.kafka_topic_creator
celery -A app.tasks.process_tasks worker --loglevel=info --pool=solo
python -m app.utils.kafka_consumer
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

