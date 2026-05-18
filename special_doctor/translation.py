from modeltranslation.translator import register, TranslationOptions
from .models import SpecialDoctor

@register(SpecialDoctor)
class SpecialDoctorTranslationOptions(TranslationOptions):
    fields = ('name', 'designation', 'doctor_fees', 'doctor_details', 'doctor_sedule', 'contact_details')
