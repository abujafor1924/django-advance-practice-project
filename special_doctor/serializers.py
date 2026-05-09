from rest_framework import serializers
from .models import SpecialCategory, SpecialHospital, SpecialDoctor, SpecialBooking, SpecialPayment

class SpecialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialCategory
        fields = ['id', 'name', 'icon']

class SpecialHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialHospital
        fields = ['id', 'name', 'address', 'contact_details']

class SpecialDoctorListSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital_name', 'category_name']

class SpecialDoctorDetailSerializer(serializers.ModelSerializer):
    hospital = SpecialHospitalSerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = SpecialDoctor
        fields = ['id', 'name', 'image', 'designation', 'years_of_experience', 'doctor_fees', 'hospital', 'category_name', 'doctor_details', 'doctor_sedule', 'contact_details']

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
