from notifications.models import Notification
from notifications.tasks import send_websocket_notification

def send_notification(user, title, message):
    """
    Utility function to send a notification to a user.
    Creates a database record and triggers a WebSocket notification.
    """
    # Create database notification
    Notification.objects.create(
        user=user,
        title=title,
        message=message
    )
    
    try:
        # Offload WebSocket notification to Celery
        send_websocket_notification.delay(user.id, title, message)
    except Exception as e:
        # Catch potential issues with Celery dispatch
        print(f"Error dispatching notification task: {e}")
