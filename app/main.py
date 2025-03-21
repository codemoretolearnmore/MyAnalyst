# app/main.py

from fastapi import FastAPI
from app.routes import prompt
# from app.utils.logger import logger
from app.utils.kafka_topic_creator import create_kafka_topics  # Import function

def create_app():
    app = FastAPI(title="GenAI Analytical Platform")

    # Ensure Kafka topics are created before starting the application
    # logger.info("Ensuring Kafka topics are created...")
    create_kafka_topics()

    app.include_router(prompt.router)
    # logger.info("Application startup initiated.")
    return app

app = create_app()

@app.get("/")
def root():
    return {"message": "GenAI Backend is running."}
