# app/utils/kafka_consumer.py

from confluent_kafka import Consumer
from app.config import KAFKA_BROKER, KAFKA_TOPICS
import json
# from app.utils.logger import logger
from ..tasks.process_tasks import (
    process_text_to_query,
    process_query_to_metrics,
    process_metrics_to_insights,
)

# Kafka Consumer Configuration
def get_kafka_consumer(group_id: str, topic: str):
    consumer = Consumer({
        "bootstrap.servers": KAFKA_BROKER,
        "group.id": group_id,
        "auto.offset.reset": "earliest",
    })
    consumer.subscribe([topic])
    return consumer

# Process Messages from Kafka
def consume_messages():
    consumer = get_kafka_consumer("genai_consumer_group", list(KAFKA_TOPICS.values()))

    try:
        while True:
            msg = consumer.poll(1.0)  # Poll every second
            if msg is None:
                continue
            if msg.error():
                # logger.error(f"Kafka error: {msg.error()}")
                continue

            topic = msg.topic()
            data = msg.value().decode("utf-8")
            data = json.loads(msg.value().decode("utf-8"))
            # logger.info(f"Received event from topic '{topic}': {data}")

            # Route messages to respective Celery tasks
            if topic == KAFKA_TOPICS["TABLES_EXTRACTED"]:
                process_text_to_query.delay(data["request_id"], data["tables"])
                print("table extracted")

            elif topic == KAFKA_TOPICS["QUERY_GENERATED"]:
                process_query_to_metrics.delay(data["request_id"], data["query"])
                print("query generated")
            elif topic == KAFKA_TOPICS["METRICS_FETCHED"]:
                process_metrics_to_insights.delay(data["request_id"], data["metrics"])
                print("All services completed")

    except Exception as e:
        print(str(e))
        # logger.error(f"Error consuming Kafka messages: {str(e)}")
    finally:
        consumer.close()

