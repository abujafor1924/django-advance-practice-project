from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'name', 'email', 'district', 'password']

    def validate_phone_number(self, value):
        phone = value.replace(" ", "").replace("-", "")
        # if not phone.startswith('+'):
        #     phone = '+' + phone
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
            is_verified=True # Automatically verified
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
