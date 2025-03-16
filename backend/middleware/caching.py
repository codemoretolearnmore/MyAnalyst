import redis
import json
from config import REDIS_HOST, REDIS_PORT

cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_cached_response(query_text: str):
    """
    Retrieves cached insights for a given query.
    """
    return cache.get(query_text)

def cache_response(query_text: str, response_data: dict, expiry=3600):
    """
    Caches insights for faster future retrieval.
    """
    cache.setex(query_text, expiry, json.dumps(response_data))
