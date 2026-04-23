from rest_framework import serializers
from .models import ServiceCategory, SubCategory, Hospital, Doctor, Booking, Payment

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'icon']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name', 'icon']

class PopularServiceHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'logo', 'address', 'contact_details']

class DoctorListSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source='hospital.name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'image', 'designation', 'hospital_name']

class DoctorDetailSerializer(serializers.ModelSerializer):
    hospital = PopularServiceHospitalSerializer(read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'image', 'designation', 'hospital', 'subcategory_name', 'doctor_details']

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['doctor', 'patient_name', 'phone', 'date', 'time']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'transaction_id', 'payment_method', 'payment_status']
        read_only_fields = ['payment_status']

class BookingListSerializer(serializers.ModelSerializer):
    doctor = DoctorListSerializer(read_only=True)
    payment = PaymentSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'doctor', 'patient_name', 'phone', 'date', 'time', 'status', 'payment']
