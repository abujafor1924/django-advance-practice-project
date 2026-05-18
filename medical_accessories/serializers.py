from rest_framework import serializers
from .models import AccessoryCategory, MedicalAccessory

class AccessoryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoryCategory
        fields = '__all__'

class MedicalAccessoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAccessory
        fields = "__all__"

class MedicalAccessoryDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = MedicalAccessory
        fields = "__all__"
