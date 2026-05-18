from rest_framework import serializers
from .models import Country, Hospital, HospitalDetail

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
