from django.test import TestCase
from popular_service.models import ServiceCategory, SubCategory, Hospital, Doctor
from popular_service.serializers import ServiceCategorySerializer, DoctorListSerializer

class SerializerTestCase(TestCase):
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

    def test_service_category_serializer(self):
        serializer = ServiceCategorySerializer(self.category)
        self.assertEqual(serializer.data['name'], 'Cardiology')

    def test_doctor_list_serializer(self):
        serializer = DoctorListSerializer(self.doctor)
        self.assertEqual(serializer.data['name'], "Dr. Smith")
        self.assertEqual(serializer.data['hospital_name'], "Apollo")
