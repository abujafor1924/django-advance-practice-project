from django.contrib import admin
from .models import Country, Hospital, HospitalDetail

class HospitalDetailInline(admin.StackedInline):
    model = HospitalDetail
    can_delete = False
    verbose_name_plural = 'Hospital Details'

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    can_delete = False
    verbose_name_plural = 'Countries'

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'speciality', 'created_at')
    list_filter = ('country', 'created_at')
    search_fields = ('name', 'country__name')
    inlines = [HospitalDetailInline]
    can_delete = False
    verbose_name_plural = 'Hospitals'

@admin.register(HospitalDetail)
class HospitalDetailAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'created_at')
    search_fields = ('hospital__name',)
    can_delete = False
    verbose_name_plural = 'Hospital Details'
