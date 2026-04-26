from django.test import TestCase
from other_medical_service.models import MedicalServiceCategory, MedicalServiceDoctor
from other_medical_service.serializers import MedicalServiceCategorySerializer, MedicalServiceDoctorSerializer

class MedicalServiceSerializersTest(TestCase):
    def setUp(self):
        self.category = MedicalServiceCategory.objects.create(
            name="Neurology",
            image="neurology.jpg"
        )
        self.doctor = MedicalServiceDoctor.objects.create(
            category=self.category,
            name="Dr. Jane",
            image="dr_jane.jpg",
            hospital="Neuro Clinic",
            doctor_details="Expert in brain surgery",
            schedule_time="Tue-Thu 9am-1pm",
            contact_number="9876543210"
        )

    def test_category_serializer(self):
        serializer = MedicalServiceCategorySerializer(instance=self.category)
        data = serializer.data
        self.assertEqual(data["name"], "Neurology")

    def test_doctor_serializer(self):
        serializer = MedicalServiceDoctorSerializer(instance=self.doctor)
        data = serializer.data
        self.assertEqual(data["name"], "Dr. Jane")
        self.assertEqual(data["category"], self.category.id)
