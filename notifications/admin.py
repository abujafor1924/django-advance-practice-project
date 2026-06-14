from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import QuoteWiserd, Notification

@admin.register(QuoteWiserd)
class QuoteWiserdAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'quote')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__phone_number', 'title', 'message')
    autocomplete_fields = ('user',)
