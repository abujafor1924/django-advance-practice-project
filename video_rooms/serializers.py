from rest_framework import serializers
from .models import Room, RoomParticipant
from django.conf import settings

User = settings.AUTH_USER_MODEL


class RoomSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'room_name', 'created_by', 'created_at')


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_name',)


class RoomParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomParticipant
        fields = ('id', 'room', 'user', 'role', 'assigned_by', 'assigned_at')
        read_only_fields = ('assigned_by', 'assigned_at')