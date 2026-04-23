from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(ServiceCategory, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='subcategory_icons/', null=True, blank=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctor_images/')
    designation = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, related_name='doctors', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='doctors', on_delete=models.CASCADE)
    doctor_details = models.TextField(null=True, blank=True)
    doctor_sedule = models.TextField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    doctor = models.ForeignKey(Doctor, related_name='bookings', on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking for {self.patient_name} with {self.doctor.name}"

class Payment(models.Model):
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
    booking = models.OneToOneField(Booking, related_name='payment', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.payment_status}"
