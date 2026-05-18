from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)
    banner = models.ImageField(upload_to='service_banners/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']

class SubCategory(models.Model):
    category = models.ForeignKey(ServiceCategory, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='subcategory_icons/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.category.name} - {self.name}"

    class Meta:
        ordering = ['id']

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctor_images/')
    designation = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField(default=0,null=True, blank=True)
    doctor_fees = models.CharField(max_length=255, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, related_name='doctors', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='doctors', on_delete=models.CASCADE)
    doctor_details = models.TextField(null=True, blank=True)
    doctor_sedule = models.TextField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
