import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Application configuration settings.
    """
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/ai_insights")
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    REDIS_BROKER = os.getenv("REDIS_BROKER", "redis://localhost:6379/0")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    RETRY_LIMIT = int(os.getenv("RETRY_LIMIT", 3))
