# core/kafka_consumer.py

from kafka import KafkaConsumer
import json
import logging
from config import settings
from services.job_service import update_job_status
from tasks.process_job import process_job

logger = logging.getLogger("kafka_consumer")

class KafkaMessageConsumer:
    def __init__(self, topic: str):
        """
        Initializes the Kafka consumer to listen for messages on a specific topic.
        """
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=settings.KAFKA_BROKER_URL,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            group_id="job-processing-group",
            auto_offset_reset="earliest"
        )

    def start_listening(self):
        """
        Starts listening for messages from Kafka and processes them.
        """
        logger.info("Kafka consumer started listening...")
        for message in self.consumer:
            try:
                data = message.value
                job_id = data.get("job_id")
                prompt = data.get("prompt")

                if not job_id or not prompt:
                    logger.error(f"Invalid message format: {data}")
                    continue
                
                logger.info(f"Received job: {job_id} with prompt: {prompt}")
                
                # Update job status to IN_PROGRESS
                update_job_status(job_id, "IN_PROGRESS")

                # Process job asynchronously
                process_job.delay(job_id, prompt)

            except Exception as e:
                logger.error(f"Error processing Kafka message: {str(e)}")

# Function to initialize consumer
def start_kafka_consumer():
    consumer = KafkaMessageConsumer(settings.KAFKA_JOB_TOPIC)
    consumer.start_listening()
