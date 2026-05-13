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

    def test_doctor_list_sorting(self):
        # Clear existing doctors to have a clean slate for sorting test
        Doctor.objects.all().delete()
        
        # Create doctors with different titles to test priority sorting
        # Priority 1: Professor
        d1 = Doctor.objects.create(
            name="Professor Alice", designation="Cardiologist",
            hospital=self.hospital, subcategory=self.subcategory
        )
        # Priority 2: Associate Professor
        d2 = Doctor.objects.create(
            name="Associate Prof. Bob", designation="Cardiologist",
            hospital=self.hospital, subcategory=self.subcategory
        )
        # Priority 3: Assistant Professor
        d3 = Doctor.objects.create(
            name="Assistant Prof. Charlie", designation="Cardiologist",
            hospital=self.hospital, subcategory=self.subcategory
        )
        # Priority 4: Default (General Doctor)
        d4 = Doctor.objects.create(
            name="Dr. Dave", designation="Cardiologist",
            hospital=self.hospital, subcategory=self.subcategory
        )
        # Priority 1: Another Professor (should come after d1 due to -id ordering if priority is same)
        d5 = Doctor.objects.create(
            name="Prof. Eve", designation="Cardiologist",
            hospital=self.hospital, subcategory=self.subcategory
        )

        url = reverse('doctor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Expected order based on priority: 1, 1, 2, 3, 4
        # Within priority 1: d5 (ID larger), d1 (ID smaller) because of order_by('priority', '-id')
        results = response.data['results']
        self.assertEqual(len(results), 5)
        self.assertEqual(results[0]['name'], "Prof. Eve")
        self.assertEqual(results[1]['name'], "Professor Alice")
        self.assertEqual(results[2]['name'], "Associate Prof. Bob")
        self.assertEqual(results[3]['name'], "Assistant Prof. Charlie")
        self.assertEqual(results[4]['name'], "Dr. Dave")

    def test_create_appointment_for_popular_doctor(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('create-appointment')
        data = {
            "doctor_id": self.doctor.id,
            "patient_name": "Test Patient",
            "patient_phone": "01700000000",
            "appointment_date": "2026-05-10",
            "appointment_time": "14:30:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['service_type'], "popular")
        self.assertEqual(response.data['patient_name'], "Test Patient")
