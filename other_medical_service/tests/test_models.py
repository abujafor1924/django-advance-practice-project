from django.test import TestCase
from other_medical_service.models import MedicalServiceCategory, MedicalServiceDoctor

class MedicalServiceModelsTest(TestCase):
    def setUp(self):
        self.category = MedicalServiceCategory.objects.create(
            name="Cardiology",
            image="test_category.jpg"
        )
        self.doctor = MedicalServiceDoctor.objects.create(
            category=self.category,
            name="Dr. Smith",
            image="dr_smith.jpg",
            hospital="City Hospital",
            doctor_details="Expert in heart surgery",
            schedule_time="Mon-Wed 10am-2pm",
            contact_number="1234567890"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Cardiology")
        self.assertEqual(str(self.category), "Cardiology")

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(self.doctor.category, self.category)
        self.assertEqual(str(self.doctor), "Dr. Smith")
