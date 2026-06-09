from rest_framework import serializers
from .models import CollaborationsCompany, Package, SocialMediaService

class CollaborationsCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaborationsCompany
        fields = "__all__"

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"

class SocialMediaServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaService
        fields = "__all__"

class SocialMediaServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaService
        fields = "__all__"
