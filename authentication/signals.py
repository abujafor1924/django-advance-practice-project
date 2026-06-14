import os
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from .models import User, Appointment

@receiver(pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `User` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = User.objects.get(pk=instance.pk).profile_picture
    except User.DoesNotExist:
        return False

    new_file = instance.profile_picture
    if not old_file == new_file:
        # Don't delete the default image
        if old_file and old_file.name != 'profile_pics/default.png' and os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `User` object is deleted.
    """
    if instance.profile_picture and instance.profile_picture.name != 'profile_pics/default.png':
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)

@receiver(post_save, sender=Appointment)
def send_appointment_notification(sender, instance, created, **kwargs):
    if created:
        from notifications.models import Notification
        from notifications.tasks import send_websocket_notification
        
        title = "New Appointment"
        message = f"Your appointment for {instance.patient_name} on {instance.appointment_date} at {instance.appointment_time} has been created."
        
        # Create database notification
        Notification.objects.create(
            user=instance.user,
            title=title,
            message=message
        )
        
        # Offload WebSocket notification to Celery
        send_websocket_notification.delay(instance.user.id, title, message)
