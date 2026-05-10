from django.test import TestCase
from popular_service.models import Hospital, SubCategory, ServiceCategory
from ..models import SpecialDoctor, SpecialBooking, SpecialPayment

class SpecialDoctorModelTest(TestCase):
    def setUp(self):
        self.service_category = ServiceCategory.objects.create(name="Health")
        self.subcategory = SubCategory.objects.create(name="Cardiology", category=self.service_category)
        self.hospital = Hospital.objects.create(name="City Hospital", address="123 Main St")
        self.doctor = SpecialDoctor.objects.create(
            name="Dr. Smith",
            designation="Senior Cardiologist",
            years_of_experience=10,
            doctor_fees="500 BDT",
            hospital=self.hospital,
            subcategory=self.subcategory
        )

    def test_special_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(self.doctor.hospital, self.hospital)
        self.assertEqual(self.doctor.subcategory, self.subcategory)
        self.assertEqual(str(self.doctor), "Dr. Smith")
