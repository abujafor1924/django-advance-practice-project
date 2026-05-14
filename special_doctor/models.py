from django.db import models
from popular_service.models import Hospital
class SpecialDoctor(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(upload_to='doctor_images/')
    designation = models.CharField(max_length=255,null=True, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0, null=True, blank=True)
    doctor_fees = models.CharField(max_length=255, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, related_name='specialist_doctors', on_delete=models.CASCADE)
    

    doctor_details = models.TextField(null=True, blank=True)
    doctor_sedule = models.TextField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
