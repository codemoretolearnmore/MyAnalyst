# app/routes/prompt.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..services.workflow import start_workflow
from pydantic import BaseModel
# from ..utils.logger import set_request_id, logger
import uuid

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/submit-prompt")
def submit_prompt():
    
    try:
        request_id = str(uuid.uuid4())
        # set_request_id(request_id)
        # prompt = request.prompt
        prompt = "Hardcoded"
        # logger.info(f"Received request {request_id} with prompt: {prompt}")
        start_workflow(request_id, prompt)
        return JSONResponse(status_code=200, content={"message":"workflow started", "request_id":request_id})
    except Exception as e:
        print(str(e))
        # logger.error(f"Error in submit_prompt: {e}")
        raise HTTPException(status_code=500, detail=str(e))
