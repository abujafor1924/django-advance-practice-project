from rest_framework import serializers
from .models import ServiceCategory, SubCategory, Hospital, Doctor

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('id', 'name', 'name_en', 'name_bn', 'icon', 'banner')

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

class PopularServiceHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"

class DoctorListSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = Doctor
        fields = "__all__"

class DoctorDetailSerializer(serializers.ModelSerializer):
    hospital = PopularServiceHospitalSerializer(read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = Doctor
        fields = "__all__"
