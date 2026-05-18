from modeltranslation.translator import register, TranslationOptions
from .models import QuoteWiserd

@register(QuoteWiserd)
class QuoteWiserdTranslationOptions(TranslationOptions):
    fields = ('title', 'quote')
