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

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'public_hospital_count', 'created_at')
    list_filter = ('country', 'created_at')
    search_fields = ('name', 'country__name')
    inlines = [HospitalDetailInline]

@admin.register(HospitalDetail)
class HospitalDetailAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'created_at')
    search_fields = ('hospital__name',)
