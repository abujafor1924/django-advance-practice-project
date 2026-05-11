from rest_framework import serializers
from .models import User, Appointment, Payment
from django.contrib.auth import authenticate
from popular_service.models import Doctor
from special_doctor.models import SpecialDoctor
from top_doctor.models import TopDoctor

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'name', 'email', 'district', 'password']

    def validate_phone_number(self, value):
        phone = value.replace(" ", "").replace("-", "")
        if len(phone) < 8 or len(phone) > 20:
            raise serializers.ValidationError("Invalid phone number length.")
        if User.objects.filter(phone_number=phone).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return phone

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            email=validated_data.get('email', ''),
            district=validated_data.get('district', ''),
            is_verified=True
        )
        return user

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(phone_number=data.get('phone_number'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid phone number or password.")
        data['user'] = user
        return data

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'name', 'email', 'district', 'profile_picture']
        read_only_fields = ['phone_number']

class ResetPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        
        if not User.objects.filter(phone_number=data.get('phone_number')).exists():
            raise serializers.ValidationError("User with this phone number does not exist.")
            
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'transaction_id', 'amount', 'method', 'status', 'created_at']

class ServiceObjectSerializer(serializers.Serializer):
    def to_representation(self, instance):
        if isinstance(instance, Doctor):
            return {
                'type': 'Popular Doctor',
                'name': instance.name,
                'designation': instance.designation,
                'hospital': instance.hospital.name if instance.hospital else None,
            }
        elif isinstance(instance, SpecialDoctor):
            return {
                'type': 'Special Doctor',
                'name': instance.name,
                'designation': instance.designation,
                'hospital': instance.hospital.name if instance.hospital else None,
            }
        elif isinstance(instance, TopDoctor):
            return {
                'type': 'Top Doctor',
                'name': instance.name,
                'designation': instance.designation,
                'hospital': instance.hospital.name if instance.hospital else None,
            }
        return str(instance)

class AppointmentSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(read_only=True)
    service_details = ServiceObjectSerializer(source='service_object', read_only=True)
    
    class Meta:
        model = Appointment
        fields = [
            'id', 'patient_name', 'patient_phone', 'appointment_date', 
            'appointment_time', 'status', 'service_type', 'created_at', 'payment', 'service_details'
        ]

class AppointmentCreateSerializer(serializers.ModelSerializer):
    service_type = serializers.ChoiceField(choices=['popular', 'special', 'top'], write_only=True)
    service_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Appointment
        fields = [
            'id', 'patient_name', 'patient_phone', 'appointment_date', 
            'appointment_time', 'service_type', 'service_id'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        service_type = validated_data.pop('service_type')
        service_id = validated_data.pop('service_id')
        user = self.context['request'].user
        
        from django.contrib.contenttypes.models import ContentType
        
        if service_type == 'popular':
            model = Doctor
        elif service_type == 'special':
            model = SpecialDoctor
        elif service_type == 'top':
            model = TopDoctor
        else:
            raise serializers.ValidationError("Invalid service type.")
            
        try:
            content_type = ContentType.objects.get_for_model(model)
            # Verify object exists
            model.objects.get(id=service_id)
        except model.DoesNotExist:
            raise serializers.ValidationError(f"{service_type.capitalize()} Doctor with id {service_id} does not exist.")
        
        appointment = Appointment.objects.create(
            user=user,
            content_type=content_type,
            object_id=service_id,
            **validated_data
        )
        return appointment
