from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import AccessoryCategory, MedicalAccessory

@admin.register(AccessoryCategory)
class AccessoryCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(MedicalAccessory)
class MedicalAccessoryAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'details')
