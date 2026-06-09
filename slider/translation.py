from modeltranslation.translator import register, TranslationOptions
from .models import SliderOne, SliderTwo

@register(SliderOne)
class SliderOneTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'alt_text')

@register(SliderTwo)
class SliderTwoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'alt_text')
