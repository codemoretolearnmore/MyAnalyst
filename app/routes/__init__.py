from fastapi import APIRouter
from app.routes import prompt  # Ensure the correct package path

router = APIRouter()

# Include individual route modules
router.include_router(prompt.router)
