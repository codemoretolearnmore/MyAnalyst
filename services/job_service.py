from core.db import get_db
from models.central_job_model import CentralJob
from utils.notification import send_webhook_notification
from datetime import datetime
from bson import ObjectId

def create_job(prompt: str) -> str:
    """Creates a new job entry in the central database and returns request_id."""
    db = next(get_db())
    request_id = str(ObjectId())
    job_entry = {
        "_id": request_id,
        "prompt": prompt,
        "status": "PENDING",
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }
    db.central_jobs.insert_one(job_entry)
    return request_id

def update_job_status(request_id: str, status: str, result: dict = None):
    """Updates job status and stores result if provided."""
    db = next(get_db())
    update_data = {"status": status, "updatedAt": datetime.utcnow()}
    if result:
        update_data["result"] = result

    db.central_jobs.update_one({"_id": request_id}, {"$set": update_data})

    if status in ["COMPLETED", "FAILED"]:
        send_webhook_notification(request_id, status)
