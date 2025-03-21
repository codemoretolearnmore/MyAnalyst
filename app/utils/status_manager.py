from ..utils.database import get_database

def update_service_status(request_id: str, service_name: str, status: str):
    db = get_database()
    db.service_status.update_one(
        {"request_id": request_id, "service": service_name},
        {"$set": {"status": status}},
        upsert=True
    )