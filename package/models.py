from django.db import models

class CollaborationsCompany(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    icon = models.ImageField(upload_to='collaborations/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Collaborations Companies"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    icon = models.ImageField(upload_to='package_icons/')
    details = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=255,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class SocialMediaService(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='social_media_icons/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Social Media Services"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
