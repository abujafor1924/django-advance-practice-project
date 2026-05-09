from django.db import models
from django.conf import settings

class TopDoctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='top_doctor_images/')
    designations = models.CharField(max_length=255)
    experience = models.CharField(max_length=100)
    fees=models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Consultation fees for the doctor",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    doctor = models.ForeignKey(TopDoctor, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='top_doctor_bookings', on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking for {self.patient_name} with {self.doctor.name}"

class Payment(models.Model):
    METHOD_CHOICES = [
        ('bkash', 'bKash'),
        ('nagad', 'Nagad'),
        ('rocket', 'Rocket'),
        ('manual', 'Manual'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    booking = models.OneToOneField(Booking, related_name='payment', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.payment_status}"
