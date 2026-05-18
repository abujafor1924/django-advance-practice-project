from modeltranslation.translator import register, TranslationOptions
from .models import MedicalServiceCategory, MedicalServiceDoctor

@register(MedicalServiceCategory)
class MedicalServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(MedicalServiceDoctor)
class MedicalServiceDoctorTranslationOptions(TranslationOptions):
    fields = ('name', 'hospital', 'doctor_details', 'schedule_time')
