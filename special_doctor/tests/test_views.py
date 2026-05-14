from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from popular_service.models import Hospital, SubCategory, ServiceCategory
from authentication.models import User, Appointment
from ..models import SpecialDoctor

class SpecialDoctorViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01711111111", password="password123")
        self.service_category = ServiceCategory.objects.create(name="Health")
        self.subcategory = SubCategory.objects.create(name="Cardiology", category=self.service_category)
        self.hospital = Hospital.objects.create(name="City Hospital", address="123 Main St")
        self.doctor = SpecialDoctor.objects.create(
            name="Dr. Smith",
            designation="Senior Cardiologist",
            years_of_experience=10,
            doctor_fees=500.00,
            hospital=self.hospital
        )

    def test_get_special_doctor_list(self):
        url = reverse('specialdoctor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_get_special_doctor_detail(self):
        url = reverse('specialdoctor-detail', args=[self.doctor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Dr. Smith")

    def test_create_appointment_for_special_doctor(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('create-appointment')
        data = {
            "doctor_id": self.doctor.id,
            "patient_name": "Jane Doe",
            "patient_phone": "01800000000",
            "appointment_date": "2026-05-15",
            "appointment_time": "11:00:00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['service_type'], "special")
