from rest_framework import serializers
from .models import SpecialDoctor
from popular_service.serializers import PopularServiceHospitalSerializer

class SpecialDoctorListSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = "__all__"

class SpecialDoctorDetailSerializer(serializers.ModelSerializer):
    hospital = PopularServiceHospitalSerializer(read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = "__all__"
