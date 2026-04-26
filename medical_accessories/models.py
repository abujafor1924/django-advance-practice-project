from django.db import models

class AccessoryCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='accessory_categories/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Accessory Categories"

    def __str__(self):
        return self.name

class MedicalAccessory(models.Model):
    category = models.ForeignKey(AccessoryCategory, related_name='accessories', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='medical_accessories/')
    details = models.TextField()
    contact_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Medical Accessories"

    def __str__(self):
        return self.name
