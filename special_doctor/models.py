from django.db import models
from popular_service.models import Hospital, SubCategory

class SpecialDoctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctor_images/')
    designation = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField(default=0, null=True, blank=True)
    doctor_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, related_name='specialist_doctors', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='specialist_doctors', on_delete=models.CASCADE)

    doctor_details = models.TextField(null=True, blank=True)
    doctor_sedule = models.TextField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class SpecialBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    doctor = models.ForeignKey(SpecialDoctor, related_name='bookings', on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.patient_name} with {self.doctor.name}"

    class Meta:
        ordering = ['-created_at']

class SpecialPayment(models.Model):
    METHOD_CHOICES = [
        ('bkash', 'bKash'),
        ('nagad', 'Nagad'),
        ('manual', 'Manual'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    booking = models.OneToOneField(SpecialBooking, related_name='payment', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES, default='manual')
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.payment_status}"
