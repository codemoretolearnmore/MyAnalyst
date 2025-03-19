from pymongo import IndexModel, ASCENDING
from datetime import datetime
from core.db import get_database

# Get MongoDB instance
db = get_database()

# Define the table information collection
table_info_collection = db["table_info"]

# Ensure indexes for fast lookup
table_info_collection.create_indexes([
    IndexModel([("request_id", ASCENDING)]),
    IndexModel([("created_at", ASCENDING)])
])

def store_table_info(request_id: str, tables: list):
    """
    Store identified table information.
    """
    data = {
        "request_id": request_id,
        "tables": tables,  # List of table names
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    table_info_collection.insert_one(data)

def get_table_info(request_id: str):
    """
    Retrieve stored table information.
    """
    return table_info_collection.find_one({"request_id": request_id}, {"_id": 0, "tables": 1})

def update_table_info(request_id: str, tables: list):
    """
    Update table information if needed.
    """
    table_info_collection.update_one(
        {"request_id": request_id},
        {"$set": {"tables": tables, "updated_at": datetime.utcnow()}}
    )
