# core/kafka_producer.py

from kafka import KafkaProducer
import json
from config import settings

class KafkaMessageProducer:
    def __init__(self):
        """
        Initializes the Kafka producer with the provided bootstrap servers.
        """
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BROKER_URL,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send_message(self, topic: str, message: dict):
        """
        Sends a message to the specified Kafka topic.
        
        Args:
            topic (str): The Kafka topic to send the message to.
            message (dict): The message payload.
        """
        self.producer.send(topic, message)
        self.producer.flush()  # Ensures the message is sent immediately

# Global instance to be used across the application
kafka_producer = KafkaMessageProducer()
