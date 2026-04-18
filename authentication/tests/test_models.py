from django.test import TestCase
from authentication.models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            phone_number="+8801712345678",
            password="password123",
            name="Test User"
        )
        self.assertEqual(user.phone_number, "+8801712345678")
        self.assertTrue(user.check_password("password123"))
        self.assertTrue(user.is_verified) # Should be True by default now
