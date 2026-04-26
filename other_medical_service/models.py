from django.db import models

class MedicalServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="service_categories/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Medical Service Categories"

    def __str__(self):
        return self.name

class MedicalServiceDoctor(models.Model):
    category = models.ForeignKey(MedicalServiceCategory, related_name="doctors", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="service_doctors/")
    hospital = models.CharField(max_length=255)
    doctor_details = models.TextField()
    schedule_time = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name






#test