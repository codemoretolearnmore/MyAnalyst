from pymongo import IndexModel, ASCENDING
from datetime import datetime
from core.db import get_database

# Get MongoDB instance
db = get_database()

# Define the central job collection
central_job_collection = db["central_jobs"]

# Ensure indexes
central_job_collection.create_indexes([
    IndexModel([("request_id", ASCENDING)], unique=True),
    IndexModel([("status", ASCENDING)]),
    IndexModel([("created_at", ASCENDING)])
])

def create_central_job(request_id: str, prompt: str):
    """
    Create a new central job entry to track the overall job status.
    """
    job_data = {
        "request_id": request_id,
        "prompt": prompt,
        "status": "PENDING",  # Initial status
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    central_job_collection.insert_one(job_data)

def update_central_job_status(request_id: str, status: str):
    """
    Update the central job's status.
    """
    central_job_collection.update_one(
        {"request_id": request_id},
        {"$set": {"status": status, "updated_at": datetime.utcnow()}}
    )

def get_central_job_status(request_id: str):
    """
    Retrieve the status of a job.
    """
    return central_job_collection.find_one({"request_id": request_id}, {"_id": 0, "status": 1})
