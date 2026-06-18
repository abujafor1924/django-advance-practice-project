import os
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from .models import User, Appointment, Payment
from notifications.utils import send_notification

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

@receiver(pre_save, sender=Appointment)
def store_previous_appointment_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._previous_status = Appointment.objects.get(pk=instance.pk).status
        except Appointment.DoesNotExist:
            instance._previous_status = None
    else:
        instance._previous_status = None

@receiver(post_save, sender=Appointment)
def send_appointment_notification(sender, instance, created, **kwargs):
    if created:
        title = "New Appointment"
        message = f"Your appointment for {instance.patient_name} on {instance.appointment_date} at {instance.appointment_time} has been created."
        send_notification(instance.user, title, message)
    
    elif hasattr(instance, '_previous_status'):
        if instance.status == 'confirmed' and instance._previous_status != 'confirmed':
            title = "Appointment Confirmed"
            message = f"Your appointment for {instance.patient_name} on {instance.appointment_date} at {instance.appointment_time} has been confirmed."
            send_notification(instance.user, title, message)

@receiver(pre_save, sender=Payment)
def store_previous_payment_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._previous_status = Payment.objects.get(pk=instance.pk).status
        except Payment.DoesNotExist:
            instance._previous_status = None
    else:
        instance._previous_status = None

@receiver(post_save, sender=Payment)
def send_payment_notification(sender, instance, created, **kwargs):
    if instance.status == 'paid' and (created or (hasattr(instance, '_previous_status') and instance._previous_status != 'paid')):
        title = "Payment Successful"
        message = f"Your payment of {instance.amount} for appointment {instance.appointment.id} has been received. Status: {instance.status}."
        send_notification(instance.appointment.user, title, message)
