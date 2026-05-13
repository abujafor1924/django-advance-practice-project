from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from package.models import CollaborationsCompany, Package

class PackageAPITests(APITestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(
            name='test_icon.png',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/png'
        )
        self.company = CollaborationsCompany.objects.create(
            name="Test Company",
            icon=self.image
        )
        self.package = Package.objects.create(
            name="Test Package",
            icon=self.image,
            details="Test details",
            contact="123456"
        )

    def test_collaborations_list(self):
        url = reverse('collaborations-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check 'results' because of pagination
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Test Company")

    def test_package_list(self):
        url = reverse('package-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check 'results' because of pagination
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], "Test Package")

    def test_package_detail(self):
        url = reverse('package-detail', args=[self.package.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Package")
        self.assertEqual(response.data['contact'], "123456")
