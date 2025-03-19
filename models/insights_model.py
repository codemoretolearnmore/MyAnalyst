from pymongo import IndexModel, ASCENDING
from datetime import datetime
from core.db import get_database

# Get MongoDB instance
db = get_database()

# Define the insights collection
insights_collection = db["insights"]

# Ensure indexes for efficient retrieval
insights_collection.create_indexes([
    IndexModel([("request_id", ASCENDING)]),
    IndexModel([("created_at", ASCENDING)])
])

def store_insights(request_id: str, insights: dict):
    """
    Store generated insights for a given request_id.
    """
    data = {
        "request_id": request_id,
        "insights": insights,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    insights_collection.insert_one(data)

def get_insights(request_id: str):
    """
    Retrieve stored insights for a given request_id.
    """
    return insights_collection.find_one({"request_id": request_id}, {"_id": 0, "insights": 1})

def update_insights(request_id: str, insights: dict):
    """
    Update insights for a given request_id.
    """
    insights_collection.update_one(
        {"request_id": request_id},
        {"$set": {"insights": insights, "updated_at": datetime.utcnow()}}
    )
