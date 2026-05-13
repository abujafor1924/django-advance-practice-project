from rest_framework import serializers
from .models import CollaborationsCompany, Package

class CollaborationsCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaborationsCompany
        fields = ['id', 'name', 'icon', 'created_at']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'icon', 'details', 'contact', 'created_at']
