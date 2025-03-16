from db.models import user_queries

async def store_query(user_id, query_text, insights):
    """
    Stores user query, response, and timestamp.
    """
    query_record = {
        "user_id": user_id,
        "query_text": query_text,
        "insights": insights,
        "timestamp": datetime.utcnow()
    }
    user_queries.insert_one(query_record)
