from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from medical_accessories.models import AccessoryCategory, MedicalAccessory

class MedicalAccessoryAPITest(APITestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(name='test.png', content=b'content', content_type='image/png')
        self.category = AccessoryCategory.objects.create(name="Test Category", image=self.image)
        self.accessory = MedicalAccessory.objects.create(
            category=self.category,
            name="Test Accessory",
            image=self.image,
            details="Test Details",
            contact_details="Test Contact"
        )

    def test_get_categories(self):
        url = reverse('accessory-category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_accessories_list(self):
        url = reverse('medical-accessory-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if only id, name, image are present in list (simplified check)
        self.assertTrue(len(response.data['results']) > 0)
        self.assertIn('name', response.data['results'][0])
        self.assertIn('image', response.data['results'][0])
        self.assertNotIn('details', response.data['results'][0])

    def test_get_accessory_detail(self):
        url = reverse('medical-accessory-detail', kwargs={'pk': self.accessory.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Accessory")
        self.assertEqual(response.data['details'], "Test Details")
