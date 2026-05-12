from django.contrib import admin
from .models import QuoteWiserd

@admin.register(QuoteWiserd)
class QuoteWiserdAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'quote')
