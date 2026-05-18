from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import SpecialDoctor

@admin.register(SpecialDoctor)
class SpecialDoctorAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'designation', 'hospital', 'years_of_experience', 'doctor_fees')
    list_filter = ('hospital',)
    search_fields = ('name', 'designation')
