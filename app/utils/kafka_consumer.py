# app/utils/kafka_consumer.py

from confluent_kafka import Consumer
from app.config import KAFKA_BROKER, KAFKA_TOPICS
import json
# from app.utils.logger import logger

print("Kafka Consumer is running...") 

from ..tasks.process_tasks import (
    process_text_to_query,
    process_query_to_metrics,
    process_metrics_to_insights,
)

# Kafka Consumer Configuration
def get_kafka_consumer(group_id: str, topics: list):
    print(f"Creating Kafka consumer for group: {group_id}, topics: {topics}")  # Debug log
    consumer = Consumer({
        "bootstrap.servers": KAFKA_BROKER,
        "group.id": group_id,
        "auto.offset.reset": "earliest",
        "security.protocol": "SASL_SSL",  # ✅ Upstash requires SASL over SSL
        "sasl.mechanism": "SCRAM-SHA-256",  # ✅ Upstash uses SCRAM-SHA-256
        "sasl.username": "connect",  # ✅ Set your Upstash Kafka username
        "sasl.password": "connect"
    })
    consumer.subscribe(topics)  # Subscribe to multiple topics
    print(f"Kafka consumer subscribed to topics: {topics}")  # Debug log
    return consumer

# Process Messages from Kafka
def consume_messages():
    print("Kafka consumer started...")  # Debug log
    consumer = get_kafka_consumer("genai_consumer_group", list(KAFKA_TOPICS.values()))
    print("Waiting for messages...")
    try:
        while True:
            msg = consumer.poll(5.0)  # Poll every 5 seconds

            if msg is None:
                # print("No message received.")  # Debug log
                continue
            if msg.error():
                print(f"Kafka Error: {msg.error()}")  # Debug log
                # logger.error(f"Kafka error: {msg.error()}")
                continue

            topic = msg.topic()
            data = msg.value().decode("utf-8")
            data = json.loads(data)
            print(f"✅ Received message from topic: {topic}, Data: {data}")  # Debug log

            # Route messages to respective Celery tasks
            if topic == "tables_extracted":
                print("🟡 Tables Information Extracted, Now triggering query generation")
                process_text_to_query.delay(data["request_id"], data["tables"])

            elif topic == "query_generated":
                print("🟡 Query generated, now triggering metrics fetch")
                process_query_to_metrics.delay(data["request_id"], data["query"])

            elif topic == "metrics_fetched":
                print("🟡 Metrics Fetched, now triggering insight generation")
                process_metrics_to_insights.delay(data["request_id"], data["metrics"])

            elif topic == "insights_created":
                print("✅ All services Completed, now saving data")

    except Exception as e:
        print(f"❌ Error: {str(e)}")  # Debug log
        # logger.error(f"Error consuming Kafka messages: {str(e)}")
    finally:
        print("Closing Kafka consumer...")  # Debug log
        consumer.close()

if __name__ == "__main__":
    consume_messages()
