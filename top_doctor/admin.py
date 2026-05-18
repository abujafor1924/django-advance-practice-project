from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import TopDoctor

@admin.register(TopDoctor)
class TopDoctorAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'designation', 'years_of_experience', 'doctor_fees','hospital', 'created_at', )
    search_fields = ('name', 'designation', 'hospital__name')
