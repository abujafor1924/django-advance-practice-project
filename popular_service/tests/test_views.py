from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from popular_service.models import ServiceCategory, SubCategory, Hospital, Doctor
from authentication.models import User

class ViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01711111111", password="password123")
        self.category = ServiceCategory.objects.create(name="Cardiology")
        self.subcategory = SubCategory.objects.create(category=self.category, name="Heart Specialist")
        self.hospital = Hospital.objects.create(name="Apollo", address="Dhaka", contact_details="123")
        self.doctor = Doctor.objects.create(
            name="Dr. Smith", 
            designation="Senior Consultant",
            hospital=self.hospital, 
            subcategory=self.subcategory,
            doctor_details="Details"
        )

    def test_get_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_doctors(self):
        url = reverse('doctor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_get_doctor_detail(self):
        url = reverse('doctor-detail', kwargs={'pk': self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Dr. Smith")

    def test_create_appointment_for_popular_doctor(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('create-appointment')
        data = {
            "service_type": "popular",
            "service_id": self.doctor.id,
            "patient_name": "Test Patient",
            "patient_phone": "01700000000",
            "appointment_date": "2026-05-10",
            "appointment_time": "14:30:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['service_type'], "popular")
        self.assertEqual(response.data['patient_name'], "Test Patient")
