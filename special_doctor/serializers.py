from rest_framework import serializers
from .models import SpecialDoctor
from popular_service.serializers import PopularServiceHospitalSerializer

class SpecialDoctorListSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital_name']

class SpecialDoctorDetailSerializer(serializers.ModelSerializer):
    hospital = PopularServiceHospitalSerializer(read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital',  'doctor_details', 'doctor_sedule', 'contact_details']
