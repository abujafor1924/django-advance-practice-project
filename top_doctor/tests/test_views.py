from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from authentication.models import User, Appointment
from top_doctor.models import TopDoctor
from datetime import date

class TopDoctorViewsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01700000000", password="password123")
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designation="Cardiologist",
            years_of_experience=10
        )
        self.doctor_list_url = reverse('top-doctor-list')
        self.create_appointment_url = reverse('create-appointment')

    def test_get_doctor_list(self):
        response = self.client.get(self.doctor_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_create_appointment_top_doctor(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "service_type": "top",
            "service_id": self.doctor.id,
            "patient_name": "John Doe",
            "patient_phone": "01800000000",
            "appointment_date": str(date.today()),
            "appointment_time": "10:00:00"
        }
        response = self.client.post(self.create_appointment_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(Appointment.objects.first().service_type, "top")
