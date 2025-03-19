import requests
import logging

logger = logging.getLogger("notification")

def send_webhook_notification(url: str, data: dict):
    """Sends a webhook notification with job status updates."""
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        logger.info(f"Webhook notification sent successfully: {data}")
    except requests.RequestException as e:
        logger.error(f"Failed to send webhook notification: {str(e)}")
