from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class AuthenticationViewsTest(APITestCase):
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
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def test_registration_view(self):
        url = reverse('register')
        response = self.client.post(url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        user = User.objects.get(phone_number="+8801712345678")
        self.assertEqual(user.profile_picture.name, 'profile_pics/default.png')

    def test_login_view(self):
        url = reverse('login')
        data = {"phone_number": "+8801712345679", "password": "password123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_profile_view(self):
        url = reverse('profile')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile_picture(self):
        url = reverse('profile')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        # Create a simple image for testing
        import io
        from PIL import Image
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        
        data = {
            "name": "Updated Name",
            "profile_picture": file
        }
        response = self.client.patch(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, "Updated Name")
        self.assertTrue(self.user.profile_picture)

    def test_reset_password_view(self):
        url = reverse('reset-password')
        data = {
            "phone_number": "+8801712345679",
            "new_password": "newpassword123",
            "confirm_password": "newpassword123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(phone_number="+8801712345679")
        self.assertTrue(user.check_password("newpassword123"))
