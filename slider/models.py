from django.db import models

class SliderOne(models.Model):
    image = models.ImageField(upload_to='sliders/', help_text="Upload image for Slider One")
    title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for Slider One")
    description = models.TextField(blank=True, null=True, help_text="Description for Slider One")
    alt_text = models.CharField(max_length=255, blank=True, null=True, help_text="Alternative text for Slider One")
    link = models.URLField(blank=True, null=True, help_text="Link for Slider One")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Slider One"
        verbose_name_plural = "Slider Ones"

    def __str__(self):
        return f"Slider One - {self.id} ({self.title or 'No Title'})"

class SliderTwo(models.Model):
    image = models.ImageField(upload_to='sliders/', help_text="Upload image for Slider Two")
    title = models.CharField(max_length=255, blank=True, null=True, help_text="Title for Slider Two")
    description = models.TextField(blank=True, null=True, help_text="Description for Slider Two")
    alt_text = models.CharField(max_length=255, blank=True, null=True, help_text="Alternative text for Slider Two")
    link = models.URLField(blank=True, null=True, help_text="Link for Slider Two")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Slider Two"
        verbose_name_plural = "Slider Twos"

    def __str__(self):
        return f"Slider Two - {self.id} ({self.title or 'No Title'})"
