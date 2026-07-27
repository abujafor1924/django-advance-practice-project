from attr import fields
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import BangladeshHospital, Country, District, Division, Hospital, HospitalDetail, InternationalCountry,InternationalGuardianHospital


class BangladeshHospitalResource(resources.ModelResource):
    division = fields.Field(attribute='division', column_name='division', widget=ForeignKeyWidget(Division, 'name'))
    district = fields.Field(attribute='district', column_name='district', widget=ForeignKeyWidget(District, 'name'))
    class Meta:
        model = BangladeshHospital
        
    def before_import_row(self, row, **kwargs):
        # Create Division if not exists
        division, _ = Division.objects.get_or_create(
            name=row["division"].strip()
        )

        # Create District if not exists
        district, _ = District.objects.get_or_create(
            division=division,
            name=row["district"].strip()
        )

        # Replace CSV value with objects for import
        row["division"] = division.name
        row["district"] = district.name


class InternationalGuardianHospitalResource(resources.ModelResource):
    country = fields.Field(
        attribute="country",
        column_name="country_en",
        widget=ForeignKeyWidget(InternationalCountry, "name"),
    )

    class Meta:
        model = InternationalGuardianHospital
        import_id_fields = ("guardian_hospital_id",)
        fields = (
            "guardian_hospital_id",
            "hospital_name",
            "country",
            "address",
            "discount",
            "contact_person",
            "contact_details",
            "cashless_facility",
        )
        skip_unchanged = True
        report_skipped = True

    def before_import_row(self, row, **kwargs):
        # Create country if it doesn't exist
        InternationalCountry.objects.get_or_create(
            name=row["country_en"].strip(),
            defaults={
                "name_en": row["country_en"].strip(),
                "name_bn": row["country_bn"].strip(),
            },
        )

        # Map translated CSV columns to model fields
        row["hospital_name"] = row["hospital_name_en"].strip()
        row["address"] = row["address_en"].strip()
        row["discount"] = row["discount_en"].strip()
        row["contact_person"] = row["contact_person_en"].strip()
        row["contact_details"] = row["contact_details_en"].strip()
        row["cashless_facility"] = row["cashless_facility_en"].strip()

class HospitalDetailInline(TranslationStackedInline):
    model = HospitalDetail
    can_delete = False
    verbose_name_plural = 'Hospital Details'

@admin.register(Country)
class CountryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    can_delete = False
    verbose_name_plural = 'Countries'
    
   

@admin.register(Hospital)
class HospitalAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'country', 'speciality', 'created_at')
    list_filter = ('country', 'created_at')
    search_fields = ('name', 'country__name')
    inlines = [HospitalDetailInline]
    can_delete = False
    verbose_name_plural = 'Hospitals'
    
    

@admin.register(HospitalDetail)
class HospitalDetailAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'hospital', 'created_at',)
    search_fields = ('hospital__name',)
    can_delete = False
    verbose_name_plural = 'Hospital Details'
    

# ============================= bangladesh hospitals admin =============================

@admin.register(Division)
class DivisionAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    can_delete = False
    verbose_name_plural = 'Divisions'
    
    
@admin.register(District)
class DistrictAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'division')
    search_fields = ('name', 'division__name')
    list_filter = ('division',)
    can_delete = False
    verbose_name_plural = 'Districts'
    

@admin.register(BangladeshHospital)
class BangladeshHospitalAdmin(ImportExportModelAdmin, TabbedTranslationAdmin):
    resource_class = BangladeshHospitalResource
    list_display = ('id', 'guardian_id', 'name', 'division', 'district')
    search_fields = ('name', 'division__name', 'district__name')
    list_filter = ('division', 'district')
    can_delete = False
    verbose_name_plural = 'Bangladesh Hospitals'
    
@admin.register(InternationalCountry)
class InternationalCountryAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    can_delete = False
    verbose_name_plural = 'International Countries'
    
    
@admin.register(InternationalGuardianHospital)
class InternationalGuardianHospitalAdmin(ImportExportModelAdmin, TabbedTranslationAdmin):
    resource_class = InternationalGuardianHospitalResource
    list_display = ('id', 'hospital_name', 'country', 'address', 'discount', 'contact_person', 'cashless_facility')
    search_fields = ('hospital_name', 'country__name', 'address', 'contact_person')
    list_filter = ('country', 'cashless_facility')
    can_delete = False
    verbose_name_plural = 'International Guardian Hospitals'