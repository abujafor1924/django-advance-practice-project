from modeltranslation.translator import register, TranslationOptions
from .models import Country, Hospital, HospitalDetail

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Hospital)
class HospitalTranslationOptions(TranslationOptions):
    fields = ('name', 'speciality')

@register(HospitalDetail)
class HospitalDetailTranslationOptions(TranslationOptions):
    fields = ('description', 'contact_info')
