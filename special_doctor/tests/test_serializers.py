from django.test import TestCase
from ..models import SpecialCategory, SpecialHospital, SpecialDoctor
from ..serializers import SpecialDoctorListSerializer, SpecialDoctorDetailSerializer

class SpecialDoctorSerializerTest(TestCase):
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

    def test_special_doctor_list_serializer(self):
        serializer = SpecialDoctorListSerializer(instance=self.doctor)
        data = serializer.data
        self.assertEqual(data['name'], "Dr. Smith")
        self.assertEqual(data['hospital_name'], "City Hospital")
        self.assertEqual(data['category_name'], "Cardiology")

    def test_special_doctor_detail_serializer(self):
        serializer = SpecialDoctorDetailSerializer(instance=self.doctor)
        data = serializer.data
        self.assertEqual(data['name'], "Dr. Smith")
        self.assertEqual(data['hospital']['name'], "City Hospital")
        self.assertEqual(data['category_name'], "Cardiology")
