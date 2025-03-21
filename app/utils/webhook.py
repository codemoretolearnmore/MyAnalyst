# app/utils/webhook.py

import requests
# from ..utils.logger import logger

def send_webhook_notification(url: str, data: dict):
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()
        # logger.info(f"Webhook notification sent successfully: {data}")
    except requests.exceptions.RequestException as e:
        print(str(e))
        # logger.error(f"Failed to send webhook notification: {e}")