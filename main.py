from fastapi import FastAPI, HTTPException, BackgroundTasks
from schemas.job_schema import JobRequest
from services.job_service import create_job
from services.status_manager import get_final_status
from services.feedback_service import store_feedback
from utils.notification import send_webhook_notification

app = FastAPI()

@app.post("/submit-prompt")
def submit_prompt(request: JobRequest, background_tasks: BackgroundTasks):
    """
    Receives user prompt, generates request_id, and starts processing in the background.
    """
    try:
        request_id = create_job(request.prompt)
        background_tasks.add_task(process_job, request_id, request.prompt)
        return {"request_id": request_id, "message": "Processing started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get-output/{request_id}")
def get_output(request_id: str):
    """
    Fetches the final output of the request.
    """
    status, result = get_final_status(request_id)
    if status == "COMPLETED":
        return {"request_id": request_id, "status": status, "result": result}
    elif status == "FAILED":
        return {"request_id": request_id, "status": status, "message": "Processing failed"}
    else:
        return {"request_id": request_id, "status": status, "message": "Processing in progress"}

@app.post("/store-feedback")
def store_user_feedback(request_id: str, feedback: str):
    """
    Stores user feedback for a specific request.
    """
    try:
        store_feedback(request_id, feedback)
        send_webhook_notification(request_id, "Feedback received")
        return {"message": "Feedback stored successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
