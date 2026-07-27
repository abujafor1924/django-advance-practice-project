from rest_framework import serializers
from .models import Country, Hospital, HospitalDetail, BangladeshHospital, Division, District, InternationalCountry, InternationalGuardianHospital

class CountrySerializer(serializers.ModelSerializer):
    hospital_count = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = "__all__"

    def get_hospital_count(self, obj) -> int:
        return obj.hospitals.count()

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"

class HospitalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalDetail
        fields = "__all__"


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ["id", "name"]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name"]


class BangladeshHospitalSerializer(serializers.ModelSerializer):
    division = DivisionSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    class Meta:
        model = BangladeshHospital
        fields = "__all__"
        
        
class InternationalCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalCountry
        fields = ["id", "name"]
    
class InternationalGuardianHospitalSerializer(serializers.ModelSerializer):
    country = InternationalCountrySerializer(read_only=True)
    class Meta:
        model = InternationalGuardianHospital
        fields = "__all__"
        
