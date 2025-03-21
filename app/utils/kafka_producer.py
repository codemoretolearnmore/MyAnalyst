from confluent_kafka import Producer
from ..config import KAFKA_CONFIG
import json
# from app.utils.logger import logger

def get_kafka_producer():
    return Producer(KAFKA_CONFIG)

def produce_event(topic: str, message: dict):
    producer = get_kafka_producer()
    if isinstance(message, str):  
        message = json.loads(message)  # Ensure it is a dictionary

    message_str = json.dumps(message)  # Convert dict to JSON string before sending
    
    producer.produce(topic, key=message["request_id"], value=message_str)
    producer.flush()
    print(f"Produced event to {topic}: {message_str}")  # Debugg
    # logger.info(f"Produced event to {topic}: {message}")