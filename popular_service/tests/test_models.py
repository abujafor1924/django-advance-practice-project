from django.test import TestCase
from popular_service.models import ServiceCategory, SubCategory, Hospital, Doctor
from authentication.models import Appointment, Payment, User
from django.contrib.contenttypes.models import ContentType

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01711111111", password="password123")
        self.category = ServiceCategory.objects.create(name="Cardiology")
        self.subcategory = SubCategory.objects.create(category=self.category, name="Heart Specialist")
        self.hospital = Hospital.objects.create(
            name="Apollo Hospital", 
            address="Dhaka", 
            contact_details="0123456789"
        )
        self.doctor = Doctor.objects.create(
            name="Dr. Smith",
            designation="Senior Consultant",
            hospital=self.hospital,
            subcategory=self.subcategory,
            doctor_details="Expert in heart surgery"
        )

    def test_service_category_creation(self):
        self.assertEqual(str(self.category), "Cardiology")

    def test_subcategory_creation(self):
        self.assertEqual(str(self.subcategory), "Cardiology - Heart Specialist")

    def test_hospital_creation(self):
        self.assertEqual(str(self.hospital), "Apollo Hospital")

    def test_doctor_creation(self):
        self.assertEqual(str(self.doctor), "Dr. Smith")

    def test_appointment_creation(self):
        appointment = Appointment.objects.create(
            user=self.user,
            content_type=ContentType.objects.get_for_model(Doctor),
            object_id=self.doctor.id,
            patient_name="John Doe",
            patient_phone="01911111111",
            appointment_date="2026-05-10",
            appointment_time="10:00:00"
        )
        self.assertEqual(appointment.service_type, "popular")
        self.assertEqual(str(appointment), f"Popular Appointment for John Doe with {self.doctor.name}")
        self.assertEqual(appointment.status, "pending")

    def test_payment_creation(self):
        appointment = Appointment.objects.create(
            user=self.user,
            content_type=ContentType.objects.get_for_model(Doctor),
            object_id=self.doctor.id,
            patient_name="John Doe",
            patient_phone="01911111111",
            appointment_date="2026-05-10",
            appointment_time="10:00:00"
        )
        payment = Payment.objects.create(
            appointment=appointment,
            transaction_id="TXN12345",
            method="bkash",
            amount=500.00
        )
        self.assertEqual(str(payment), f"Payment for Appointment {appointment.id} - pending")
