from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import MedicalServiceCategory, MedicalServiceDoctor

@admin.register(MedicalServiceCategory)
class MedicalServiceCategoryAdmin(TabbedTranslationAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(MedicalServiceDoctor)
class MedicalServiceDoctorAdmin(TabbedTranslationAdmin):
    list_display = ("name", "category", "hospital", "schedule_time", "contact_number")
    list_filter = ("category", "hospital")
    search_fields = ("name", "hospital", "contact_number")
