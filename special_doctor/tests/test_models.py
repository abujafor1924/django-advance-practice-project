from django.test import TestCase
from ..models import SpecialCategory, SpecialHospital, SpecialDoctor

class SpecialDoctorModelTest(TestCase):
    def setUp(self):
        self.category = SpecialCategory.objects.create(name="Cardiology")
        self.hospital = SpecialHospital.objects.create(name="City Hospital", address="123 Main St")
        self.doctor = SpecialDoctor.objects.create(
            name="Dr. Smith",
            designation="Senior Cardiologist",
            years_of_experience=10,
            doctor_fees=500.00,
            hospital=self.hospital,
            category=self.category
        )

    def test_special_category_creation(self):
        self.assertEqual(self.category.name, "Cardiology")
        self.assertEqual(str(self.category), "Cardiology")

    def test_special_hospital_creation(self):
        self.assertEqual(self.hospital.name, "City Hospital")
        self.assertEqual(str(self.hospital), "City Hospital")

    def test_special_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(self.doctor.hospital, self.hospital)
        self.assertEqual(self.doctor.category, self.category)
        self.assertEqual(str(self.doctor), "Dr. Smith")
