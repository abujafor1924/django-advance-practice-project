from modeltranslation.translator import register, TranslationOptions
from .models import TopDoctor

@register(TopDoctor)
class TopDoctorTranslationOptions(TranslationOptions):
    fields = ('name', 'designation', 'doctor_fees', 'doctor_details', 'doctor_sedule', 'contact_details')
