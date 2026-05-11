from django.contrib import admin
from .models import SpecialDoctor

@admin.register(SpecialDoctor)
class SpecialDoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'hospital', 'subcategory', 'years_of_experience', 'doctor_fees')
    list_filter = ('hospital', 'subcategory')
    search_fields = ('name', 'designation')
