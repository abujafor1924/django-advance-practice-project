from rest_framework import serializers
from .models import MedicalServiceCategory, MedicalServiceDoctor

class MedicalServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalServiceCategory
        fields = "__all__"

class MedicalServiceDoctorSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    
    class Meta:
        model = MedicalServiceDoctor
        fields = "__all__"
