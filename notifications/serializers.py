from rest_framework import serializers
from .models import QuoteWiserd, Notification

class QuoteWiserdSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteWiserd
        fields = "__all__"
        read_only_fields = ['created_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'is_read', 'created_at']
        read_only_fields = ['created_at']
