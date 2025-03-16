from fastapi import FastAPI, Depends
from pydantic import BaseModel
from services.query_service import process_user_query
from services.feedback_service import store_feedback

app = FastAPI()

class QueryRequest(BaseModel):
    user_id: str
    query_text: str

class FeedbackRequest(BaseModel):
    user_id: str
    query_id: str
    feedback: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    """
    Handles user query processing and returns insights.
    """
    insights = await process_user_query(request.user_id, request.query_text)
    return {"insights": insights}

@app.post("/feedback")
async def handle_feedback(request: FeedbackRequest):
    """
    Handles storing user feedback on insights.
    """
    await store_feedback(request.user_id, request.query_id, request.feedback)
    return {"message": "Feedback recorded successfully"}
