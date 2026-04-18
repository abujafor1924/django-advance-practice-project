from rest_framework import serializers
from .models import Country, Hospital, HospitalDetail

class CountrySerializer(serializers.ModelSerializer):
    hospital_count = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ['id', 'name', 'flag', 'hospital_count']

    def get_hospital_count(self, obj) -> int:
        return obj.hospitals.count()

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'icon', 'agreement_status', 'public_hospital_count', 'country']

class HospitalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalDetail
        fields = ['id', 'hospital', 'banner', 'description', 'contact_info']
