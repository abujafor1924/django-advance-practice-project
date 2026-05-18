from rest_framework import serializers
from .models import QuoteWiserd

class QuoteWiserdSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteWiserd
        fields = "__all__"
        read_only_fields = ['created_at']
