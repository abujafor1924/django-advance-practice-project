from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import SliderOne, SliderTwo

@admin.register(SliderOne)
class SliderOneAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'image', 'title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'id')

@admin.register(SliderTwo)
class SliderTwoAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'image', 'title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'id')
