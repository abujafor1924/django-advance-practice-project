from modeltranslation.translator import register, TranslationOptions
from .models import ServiceCategory, SubCategory, Hospital, Doctor

@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Hospital)
class HospitalTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'contact_details')

@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('name', 'designation', 'doctor_details')
