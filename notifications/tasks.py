from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def send_websocket_notification(user_id, title, message):
    channel_layer = get_channel_layer()
    group_name = f"user_{user_id}"
    
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "send_notification",
            "title": title,
            "message": message,
        }
    )
