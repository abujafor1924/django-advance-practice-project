from modeltranslation.translator import register, TranslationOptions
from .models import CollaborationsCompany, Package, SocialMediaService

@register(CollaborationsCompany)
class CollaborationsCompanyTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Package)
class PackageTranslationOptions(TranslationOptions):
    fields = ('name', 'details', 'contact')

@register(SocialMediaService)
class SocialMediaServiceTranslationOptions(TranslationOptions):
    fields = ('name',)
