from django.test import TestCase
from popular_service.models import Hospital, SubCategory, ServiceCategory
from authentication.models import User, Appointment, Payment
from django.contrib.contenttypes.models import ContentType
from ..models import SpecialDoctor

class SpecialDoctorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01711111111", password="password123")
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

    def test_special_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(str(self.doctor), "Dr. Smith")

    def test_special_appointment_creation(self):
        appointment = Appointment.objects.create(
            user=self.user,
            content_type=ContentType.objects.get_for_model(SpecialDoctor),
            object_id=self.doctor.id,
            patient_name="Jane Doe",
            patient_phone="01822222222",
            appointment_date="2026-05-12",
            appointment_time="11:00:00"
        )
        self.assertEqual(appointment.service_type, "special")
        self.assertEqual(str(appointment), f"Special Appointment for Jane Doe with {self.doctor.name}")
