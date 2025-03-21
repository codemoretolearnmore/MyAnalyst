import os
# import logging
from confluent_kafka.admin import AdminClient, NewTopic
from app.config import KAFKA_BROKER, KAFKA_SECURITY_PROTOCOL,KAFKA_SECURITY_MECHANISM,KAFKA_USERNAME,KAFKA_PASSWORD, KAFKA_TOPICS


def create_kafka_topics():
    """Creates Kafka topics if they don't exist"""
    
    # Kafka Config - Modify if using SASL/SSL
    kafka_config = {
        "bootstrap.servers": KAFKA_BROKER,
        "security.protocol": KAFKA_SECURITY_PROTOCOL,
        "sasl.mechanism": KAFKA_SECURITY_MECHANISM,
        "sasl.username": KAFKA_USERNAME,
        "sasl.password": KAFKA_PASSWORD,

    }
    

    admin_client = AdminClient(kafka_config)
    
    # Get existing topics
    existing_topics = admin_client.list_topics().topics.keys()
    
    new_topics = [
        NewTopic(topic, num_partitions=1, replication_factor=3)
        for topic in KAFKA_TOPICS.values() if topic not in existing_topics
    ]
    
    if new_topics:
        # Create topics
        futures = admin_client.create_topics(new_topics)

        # Wait for topic creation confirmation
        for topic, future in futures.items():
            try:
                future.result()  # The result() will raise an exception if topic creation failed
             
            except Exception as e:
                print(str(e))
              
    else:
       print("no changed been made")

if __name__ == "__main__":
    create_kafka_topics()
