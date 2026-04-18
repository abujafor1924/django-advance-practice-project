from rest_framework import serializers
from .models import SliderOne, SliderTwo

class SliderOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderOne
        fields = ['id', 'image', 'created_at']
        read_only_fields = ['created_at']

    def validate_image(self, value):
        # Basic validation example: restrict file size to 5MB
        limit = 5 * 1024 * 1024
        if value.size > limit:
            raise serializers.ValidationError("Image file too large ( > 5MB )")
        return value

class SliderTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderTwo
        fields = ['id', 'image', 'created_at']
        read_only_fields = ['created_at']

    def validate_image(self, value):
        # Basic validation example: restrict file size to 5MB
        limit = 5 * 1024 * 1024
        if value.size > limit:
            raise serializers.ValidationError("Image file too large ( > 5MB )")
        return value
