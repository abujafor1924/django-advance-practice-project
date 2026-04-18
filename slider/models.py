from django.db import models

class SliderOne(models.Model):
    image = models.ImageField(upload_to='sliders/', help_text="Upload image for Slider One")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Slider One"
        verbose_name_plural = "Slider Ones"

    def __str__(self):
        return f"Slider One - {self.id}"

class SliderTwo(models.Model):
    image = models.ImageField(upload_to='sliders/', help_text="Upload image for Slider Two")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Slider Two"
        verbose_name_plural = "Slider Twos"

    def __str__(self):
        return f"Slider Two - {self.id}"
