from rest_framework import serializers
from .models import TopDoctor, Booking, Payment

class TopDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopDoctor
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'status']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['payment_status']

class BookingDetailSerializer(serializers.ModelSerializer):
    doctor = TopDoctorSerializer(read_only=True)
    payment = PaymentSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
