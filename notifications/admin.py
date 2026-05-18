from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import QuoteWiserd

@admin.register(QuoteWiserd)
class QuoteWiserdAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'quote')
