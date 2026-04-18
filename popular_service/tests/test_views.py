from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from popular_service.models import ServiceCategory, SubCategory, Hospital, Doctor, Booking

class ViewTestCase(APITestCase):
    def setUp(self):
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
        self.assertEqual(len(response.data), 1)

    def test_get_doctors(self):
        url = reverse('doctor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if results are in pagination response
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_doctor_detail(self):
        url = reverse('doctor-detail', kwargs={'pk': self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Dr. Smith")

    def test_create_booking(self):
        url = reverse('booking-create')
        data = {
            "doctor": self.doctor.id,
            "patient_name": "Test Patient",
            "phone": "01700000000",
            "date": "2026-05-10",
            "time": "14:30:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('booking_id', response.data)
        self.assertIn('payment_instructions', response.data)
