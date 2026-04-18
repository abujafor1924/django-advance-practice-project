from django.contrib import admin
from .models import SliderOne, SliderTwo

@admin.register(SliderOne)
class SliderOneAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)

@admin.register(SliderTwo)
class SliderTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)
