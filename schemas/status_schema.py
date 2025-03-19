from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class StatusUpdate(BaseModel):
    request_id: str
    service: str
    status: str
    updated_at: datetime
    error_message: Optional[str] = None
