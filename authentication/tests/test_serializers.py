from django.test import TestCase
from authentication.serializers import (
    UserRegistrationSerializer, LoginSerializer,
    ProfileSerializer, ResetPasswordSerializer
)
from authentication.models import User

class SerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            "phone_number": "+8801712345678",
            "password": "password123",
            "name": "Test User",
            "email": "test@example.com"
        }
        self.user = User.objects.create_user(
            phone_number="+8801712345679",
            password="password123"
        )

    def test_registration_serializer(self):
        serializer = UserRegistrationSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.phone_number, self.user_data['phone_number'])
        self.assertTrue(user.is_verified)

    def test_login_serializer(self):
        data = {"phone_number": "+8801712345679", "password": "password123"}
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_reset_password_serializer(self):
        data = {
            "phone_number": "+8801712345679",
            "new_password": "newpassword123",
            "confirm_password": "newpassword123"
        }
        serializer = ResetPasswordSerializer(data=data)
        self.assertTrue(serializer.is_valid())
