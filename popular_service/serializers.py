from rest_framework import serializers
from .models import ServiceCategory, SubCategory, Hospital, Doctor

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'icon']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name', 'icon']

class PopularServiceHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name']

class DoctorListSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital_name', 'subcategory_name']

class DoctorDetailSerializer(serializers.ModelSerializer):
    hospital = PopularServiceHospitalSerializer(read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital', 'subcategory_name', 'doctor_details', 'doctor_sedule', 'contact_details']
