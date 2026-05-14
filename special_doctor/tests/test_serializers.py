from django.test import TestCase
from popular_service.models import Hospital, SubCategory, ServiceCategory
from ..models import SpecialDoctor
from ..serializers import SpecialDoctorListSerializer, SpecialDoctorDetailSerializer

class SpecialDoctorSerializerTest(TestCase):
    def setUp(self):
        self.service_category = ServiceCategory.objects.create(name="Health")
        self.subcategory = SubCategory.objects.create(name="Cardiology", category=self.service_category)
        self.hospital = Hospital.objects.create(name="City Hospital", address="123 Main St")
        self.doctor = SpecialDoctor.objects.create(
            name="Dr. Smith",
            designation="Senior Cardiologist",
            years_of_experience=10,
            doctor_fees="500 BDT",
            hospital=self.hospital
        )

    def test_special_doctor_list_serializer(self):
        serializer = SpecialDoctorListSerializer(instance=self.doctor)
        data = serializer.data
        self.assertEqual(data['name'], "Dr. Smith")
        self.assertEqual(data['hospital_name'], "City Hospital")

    def test_special_doctor_detail_serializer(self):
        serializer = SpecialDoctorDetailSerializer(instance=self.doctor)
        data = serializer.data
        self.assertEqual(data['name'], "Dr. Smith")
        self.assertEqual(data['hospital']['name'], "City Hospital")
