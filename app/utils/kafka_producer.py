from confluent_kafka import Producer
from ..config import KAFKA_BROKER
# from app.utils.logger import logger

def get_kafka_producer():
    return Producer({"bootstrap.servers": KAFKA_BROKER})

def produce_event(topic: str, message: dict):
    producer = get_kafka_producer()
    producer.produce(topic, key=message["request_id"], value=str(message))
    producer.flush()
    # logger.info(f"Produced event to {topic}: {message}")