from django.contrib import admin
from .models import CollaborationsCompany, Package, SocialMediaServices

@admin.register(CollaborationsCompany)
class CollaborationsCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'created_at')
    search_fields = ('name', 'contact')

@admin.register(SocialMediaServices)
class SocialMediaServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
