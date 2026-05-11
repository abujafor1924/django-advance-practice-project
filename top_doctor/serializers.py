from rest_framework import serializers
from .models import TopDoctor

class TopDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopDoctor
        fields = '__all__'
