from pymongo import MongoClient
from config import MONGO_URI

class Database:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client.get_database()

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        self.client.close()

# Create a global database instance
db_instance = Database()

def get_db():
    """Returns the database instance."""
    return db_instance