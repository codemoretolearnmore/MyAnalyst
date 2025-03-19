from pymongo import MongoClient, ASCENDING
import os
import logging
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB_NAME", "insights_db")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("migrations")

def apply_migrations():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]

    migrations = [
        {
            "collection": "central_jobs",
            "indexes": [("request_id", ASCENDING), ("created_at", ASCENDING)]
        },
        {
            "collection": "table_info",
            "indexes": [("request_id", ASCENDING)]
        },
        {
            "collection": "queries",
            "indexes": [("request_id", ASCENDING)]
        },
        {
            "collection": "metrics",
            "indexes": [("request_id", ASCENDING)]
        },
        {
            "collection": "insights",
            "indexes": [("request_id", ASCENDING)]
        }
    ]

    for migration in migrations:
        collection_name = migration["collection"]
        indexes = migration["indexes"]

        collection = db[collection_name]
        for index in indexes:
            collection.create_index([index])
            logger.info(f"Created index {index} on {collection_name}")

    logger.info("All migrations applied successfully!")

if __name__ == "__main__":
    apply_migrations()
