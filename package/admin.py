from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import CollaborationsCompany, Package, SocialMediaService

@admin.register(CollaborationsCompany)
class CollaborationsCompanyAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Package)
class PackageAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'contact', 'created_at')
    search_fields = ('name', 'contact')

@admin.register(SocialMediaService)
class SocialMediaServiceAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
