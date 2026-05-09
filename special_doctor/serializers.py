from rest_framework import serializers
from .models import SpecialDoctor, SpecialBooking, SpecialPayment
from popular_service.serializers import PopularServiceHospitalSerializer

class SpecialDoctorListSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital_name', 'subcategory_name']

class SpecialDoctorDetailSerializer(serializers.ModelSerializer):
    hospital = PopularServiceHospitalSerializer(read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital', 'subcategory_name', 'doctor_details', 'doctor_sedule', 'contact_details']

class SpecialPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialPayment
        fields = ['id', 'booking', 'transaction_id', 'payment_method', 'payment_status']
        read_only_fields = ['payment_status']

class SpecialBookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialBooking
        fields = ['id', 'doctor', 'patient_name', 'phone', 'date', 'time']

class SpecialBookingListSerializer(serializers.ModelSerializer):
    doctor = SpecialDoctorListSerializer(read_only=True)
    payment = SpecialPaymentSerializer(read_only=True)

    class Meta:
        model = SpecialBooking
        fields = ['id', 'doctor', 'patient_name', 'phone', 'date', 'time', 'status', 'payment', 'created_at']
