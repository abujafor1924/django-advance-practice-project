from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import ServiceCategory, SubCategory, Hospital, Doctor

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'icon', 'banner')
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'category', 'name', 'icon')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Hospital)
class HospitalAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name')

@admin.register(Doctor)
class DoctorAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'designation', 'years_of_experience', 'doctor_fees', 'hospital', 'subcategory')
    list_filter = ('hospital', 'subcategory')
    search_fields = ('name', 'designation')
    fields = ('name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital', 'subcategory', 'doctor_details', 'doctor_sedule', 'contact_details')
