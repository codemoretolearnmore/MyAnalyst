from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobRequest(BaseModel):
    prompt: str

class JobResponse(BaseModel):
    request_id: str
    status: str
    created_at: datetime

class JobUpdate(BaseModel):
    status: str
    result: Optional[dict] = None
    updated_at: datetime
