from db.database import get_db
from utils.helpers import perform_analysis

async def generate_insights(intent: str, db):
    """
    Fetches data, applies calculations, and returns insights.
    """
    # Fetch relevant data based on intent
    data = db.get_data_for_intent(intent)

    # Perform analysis
    insights = perform_analysis(data)

    return insights
