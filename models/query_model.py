from pymongo import IndexModel, ASCENDING
from datetime import datetime
from core.db import get_database

# Get MongoDB instance
db = get_database()

# Define the query collection
query_collection = db["queries"]

# Ensure indexes for efficient query lookup
query_collection.create_indexes([
    IndexModel([("request_id", ASCENDING)]),
    IndexModel([("created_at", ASCENDING)])
])

def store_query(request_id: str, sql_query: str):
    """
    Store the generated SQL query for the given request_id.
    """
    data = {
        "request_id": request_id,
        "sql_query": sql_query,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    query_collection.insert_one(data)

def get_query(request_id: str):
    """
    Retrieve the stored SQL query for a given request_id.
    """
    return query_collection.find_one({"request_id": request_id}, {"_id": 0, "sql_query": 1})

def update_query(request_id: str, sql_query: str):
    """
    Update the SQL query for a request if needed.
    """
    query_collection.update_one(
        {"request_id": request_id},
        {"$set": {"sql_query": sql_query, "updated_at": datetime.utcnow()}}
    )
