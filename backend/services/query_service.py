from db.database import get_db
from services.insight_service import generate_insights
from services.model_service import get_intent
from utils.helpers import store_query
from utils.validation import validate_query
from middleware.caching import get_cached_response, cache_response

async def process_user_query(user_id: str, query_text: str):
    """
    Processes user query:
    1. Checks cache.
    2. Identifies intent.
    3. Fetches required data.
    4. Generates insights.
    5. Stores query-response for learning.
    """

    # Validate user query
    if not validate_query(query_text):
        return {"error": "Invalid query format."}

    # Check cache first
    cached_response = get_cached_response(query_text)
    if cached_response:
        return cached_response

    db = get_db()

    # Identify user intent
    intent = await get_intent(query_text)

    # Fetch relevant data & generate insights
    insights = await generate_insights(intent, db)

    # Store user query and generated insights for future training
    await store_query(user_id, query_text, insights)

    # Cache response
    cache_response(query_text, insights)

    return insights
