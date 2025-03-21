from pymongo import MongoClient
from ..config import MONGO_URI

def get_database():
    client = MongoClient(MONGO_URI)
    return client.get_database()