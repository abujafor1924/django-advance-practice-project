from rest_framework import serializers
from .models import SliderOne, SliderTwo

# Slider One Serializers
class SliderOneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderOne
        fields = ['id', 'image']

class SliderOneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderOne
        fields = [
            'id', 'image', 'title', 'title_en', 'title_bn',
            'description', 'description_en', 'description_bn',
            'alt_text', 'alt_text_en', 'alt_text_bn',
            'link', 'created_at'
        ]
        read_only_fields = ['created_at']

    def validate_image(self, value):
        limit = 5 * 1024 * 1024
        if value.size > limit:
            raise serializers.ValidationError("Image file too large ( > 5MB )")
        return value

# Slider Two Serializers
class SliderTwoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderTwo
        fields = ['id', 'image']

class SliderTwoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderTwo
        fields = [
            'id', 'image', 'title', 'title_en', 'title_bn',
            'description', 'description_en', 'description_bn',
            'alt_text', 'alt_text_en', 'alt_text_bn',
            'link', 'created_at'
        ]
        read_only_fields = ['created_at']

    def validate_image(self, value):
        limit = 5 * 1024 * 1024
        if value.size > limit:
            raise serializers.ValidationError("Image file too large ( > 5MB )")
        return value
