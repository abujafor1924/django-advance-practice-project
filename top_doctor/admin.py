from django.contrib import admin
from .models import TopDoctor

@admin.register(TopDoctor)
class TopDoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'years_of_experience', 'doctor_fees','hospital', 'created_at', )
    search_fields = ('name', 'designation', 'hospital__name')
