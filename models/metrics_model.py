from pymongo import IndexModel, ASCENDING
from datetime import datetime
from core.db import get_database

# Get MongoDB instance
db = get_database()

# Define the metrics collection
metrics_collection = db["metrics"]

# Ensure indexes for efficient metric lookup
metrics_collection.create_indexes([
    IndexModel([("request_id", ASCENDING)]),
    IndexModel([("created_at", ASCENDING)])
])

def store_metrics(request_id: str, metrics: dict):
    """
    Store calculated metrics for a given request_id.
    """
    data = {
        "request_id": request_id,
        "metrics": metrics,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    metrics_collection.insert_one(data)

def get_metrics(request_id: str):
    """
    Retrieve the stored metrics for a given request_id.
    """
    return metrics_collection.find_one({"request_id": request_id}, {"_id": 0, "metrics": 1})

def update_metrics(request_id: str, metrics: dict):
    """
    Update metrics for a given request_id.
    """
    metrics_collection.update_one(
        {"request_id": request_id},
        {"$set": {"metrics": metrics, "updated_at": datetime.utcnow()}}
    )
