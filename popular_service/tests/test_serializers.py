from django.test import TestCase
from popular_service.models import ServiceCategory, SubCategory, Hospital, Doctor, Booking
from popular_service.serializers import ServiceCategorySerializer, DoctorListSerializer, BookingCreateSerializer

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
        expected_data = {'id': self.category.id, 'name': 'Cardiology', 'icon': None}
        self.assertEqual(serializer.data, expected_data)

    def test_doctor_list_serializer(self):
        serializer = DoctorListSerializer(self.doctor)
        self.assertEqual(serializer.data['name'], "Dr. Smith")
        self.assertEqual(serializer.data['hospital_name'], "Apollo")

    def test_booking_create_serializer_valid(self):
        data = {
            "doctor": self.doctor.id,
            "patient_name": "Test Patient",
            "phone": "01700000000",
            "date": "2026-05-10",
            "time": "14:30:00"
        }
        serializer = BookingCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
