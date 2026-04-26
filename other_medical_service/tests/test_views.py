from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from other_medical_service.models import MedicalServiceCategory, MedicalServiceDoctor

class MedicalServiceViewsTest(APITestCase):
    def setUp(self):
        self.category = MedicalServiceCategory.objects.create(
            name="General Medicine",
            image="general.jpg"
        )
        self.doctor = MedicalServiceDoctor.objects.create(
            category=self.category,
            name="Dr. Brown",
            image="dr_brown.jpg",
            hospital="Public Clinic",
            doctor_details="General Physician",
            schedule_time="Friday 4pm-8pm",
            contact_number="555666777"
        )

    def test_get_categories(self):
        url = reverse("category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_get_doctors(self):
        url = reverse("doctor-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
