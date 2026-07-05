from modeltranslation.translator import register, TranslationOptions
from .models import BangladeshHospital, Country, District, Division, Hospital, HospitalDetail

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Hospital)
class HospitalTranslationOptions(TranslationOptions):
    fields = ('name', 'speciality')

@register(HospitalDetail)
class HospitalDetailTranslationOptions(TranslationOptions):
    fields = ('description', 'contact_info')


@register(Division)
class DivisionTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(BangladeshHospital)
class BangladeshHospitalTranslationOptions(TranslationOptions):
    fields = (
        
        "name",
        "address",
        "facilities",
        "contact_details",
        "remark",
        )

@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)