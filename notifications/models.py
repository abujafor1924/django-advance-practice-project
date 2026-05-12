from django.db import models

class QuoteWiserd(models.Model):
    title = models.CharField(max_length=255)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Quote Wiserd'
        verbose_name_plural = 'Quote Wiserds'

    def __str__(self):
        return self.title
