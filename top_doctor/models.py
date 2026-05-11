from django.db import models
from django.conf import settings

class TopDoctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctor_images/')
    designation = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField(default=0,null=True, blank=True)
    doctor_fees = models.CharField(max_length=255, null=True, blank=True)
    hospital = models.ForeignKey('popular_service.Hospital', related_name='top_doctors', on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey('popular_service.SubCategory', related_name='top_doctors', on_delete=models.CASCADE, null=True, blank=True)
    doctor_details = models.TextField(null=True, blank=True)
    doctor_sedule = models.TextField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
