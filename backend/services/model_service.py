from config import MODEL_NAME

async def get_intent(query_text: str):
    """
    Uses LLM to determine the intent of the query.
    """
    # This should call your fine-tuned model or local LLM
    model_response = some_model_call(MODEL_NAME, query_text)
    return model_response["intent"]
