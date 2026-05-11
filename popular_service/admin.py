from django.contrib import admin
from .models import ServiceCategory, SubCategory, Hospital, Doctor

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'icon')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'years_of_experience', 'doctor_fees', 'hospital', 'subcategory')
    list_filter = ('hospital', 'subcategory')
    search_fields = ('name', 'designation')
    fields = ('name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital', 'subcategory', 'doctor_details', 'doctor_sedule', 'contact_details')
