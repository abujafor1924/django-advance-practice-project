from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils import timezone
from datetime import timedelta
from authentication.models import Appointment

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

@shared_task
def check_appointment_reminders():
    """
    Task to check for upcoming appointments and send reminders:
    - 14 hours before appointment
    - 2 hours before appointment
    """
    now = timezone.now()
    
    # 14 hours reminder
    reminder_14h_time = now + timedelta(hours=14)
    upcoming_14h = Appointment.objects.filter(
        appointment_date=reminder_14h_time.date(),
        appointment_time__lte=reminder_14h_time.time(),
        status='confirmed',
        reminder_14h_sent=False
    )
    
    for appointment in upcoming_14h:
        # Extra check for the time range (e.g., within the next hour)
        # Assuming task runs every 10-30 mins
        title = "Appointment Reminder (14h)"
        message = f"Your appointment for {appointment.patient_name} is scheduled for tomorrow at {appointment.appointment_time}."
        from .utils import send_notification
        send_notification(appointment.user, title, message)
        appointment.reminder_14h_sent = True
        appointment.save(update_fields=['reminder_14h_sent'])

    # 2 hours reminder
    reminder_2h_time = now + timedelta(hours=2)
    upcoming_2h = Appointment.objects.filter(
        appointment_date=reminder_2h_time.date(),
        appointment_time__lte=reminder_2h_time.time(),
        status='confirmed',
        reminder_2h_sent=False
    )
    
    for appointment in upcoming_2h:
        title = "Appointment Reminder (2h)"
        message = f"Your appointment for {appointment.patient_name} starts in 2 hours at {appointment.appointment_time}."
        from .utils import send_notification
        send_notification(appointment.user, title, message)
        appointment.reminder_2h_sent = True
        appointment.save(update_fields=['reminder_2h_sent'])
