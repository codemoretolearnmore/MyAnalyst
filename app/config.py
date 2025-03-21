# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "insights_db")

# Kafka Configuration
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_SECURITY_PROTOCOL = os.getenv("KAFKA_SECURITY_PROTOCOL", "SASL_SSL")
KAFKA_SECURITY_MECHANISM = os.getenv("SASL_MECHANISM", "SCRAM-SHA-256")
KAFKA_USERNAME = os.getenv("KAFKA_USERNAME", "connect")
KAFKA_PASSWORD = os.getenv("KAFKA_PASSWORD", "connect")
KAFKA_TOPICS = {
    "TABLES_EXTRACTED": "tables_extracted",
    "QUERY_GENERATED": "query_generated",
    "METRICS_FETCHED": "metrics_fetched",
    "INSIGHTS_CREATED": "insights_created"
}

KAFKA_CONFIG = {
    "bootstrap.servers": "cve5b9gt5iv26e6990q0.any.us-east-1.mpx.prd.cloud.redpanda.com:9092",
    "security.protocol": "SASL_SSL",  # Required for Redpanda Cloud
    "sasl.mechanisms": "SCRAM-SHA-256",
    "sasl.username": "connect",
    "sasl.password": "connect",
}

# Celery Configuration
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_BACKEND_URL = os.getenv("CELERY_BACKEND_URL", "redis://localhost:6379/0")