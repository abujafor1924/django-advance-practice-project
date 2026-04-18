from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from foreign_treatments.models import Country, Hospital, HospitalDetail

class ForeignTreatmentsViewTest(APITestCase):
    def setUp(self):
        self.flag = SimpleUploadedFile(name='test_flag.png', content=b'content', content_type='image/png')
        self.country = Country.objects.create(name="Test Country", flag=self.flag)
        self.icon = SimpleUploadedFile(name='test_icon.png', content=b'content', content_type='image/png')
        self.hospital = Hospital.objects.create(
            country=self.country,
            name="Test Hospital",
            icon=self.icon,
            agreement_status="Done"
        )
        self.banner = SimpleUploadedFile(name='test_banner.png', content=b'content', content_type='image/png')
        self.hospital_detail = HospitalDetail.objects.create(
            hospital=self.hospital,
            banner=self.banner,
            description="Test Description",
            contact_info="Test Contact Info"
        )

    def test_country_list_view(self):
        url = reverse('country-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check within results due to pagination
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], self.country.name)

    def test_country_retrieve_view(self):
        url = reverse('country-detail', args=[self.country.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.country.name)

    def test_country_hospital_list_view(self):
        url = reverse('country-hospitals', args=[self.country.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], self.hospital.name)

    def test_hospital_list_view(self):
        url = reverse('hospital-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_hospital_retrieve_view(self):
        url = reverse('hospital-detail', args=[self.hospital.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.hospital.name)

    def test_hospital_detail_retrieve_view(self):
        url = reverse('hospital-detail-info', args=[self.hospital.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], self.hospital_detail.description)
