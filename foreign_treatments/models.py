from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class Hospital(models.Model):
    country = models.ForeignKey(Country, related_name='hospitals', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='hospital_icons/')
    public_hospital_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class HospitalDetail(models.Model):
    hospital = models.OneToOneField(Hospital, related_name='details', on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='hospital_banners/')
    description = models.TextField()
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Details for {self.hospital.name}"
