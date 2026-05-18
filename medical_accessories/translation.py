from modeltranslation.translator import register, TranslationOptions
from .models import AccessoryCategory, MedicalAccessory

@register(AccessoryCategory)
class AccessoryCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(MedicalAccessory)
class MedicalAccessoryTranslationOptions(TranslationOptions):
    fields = ('name', 'details', 'contact_details')
