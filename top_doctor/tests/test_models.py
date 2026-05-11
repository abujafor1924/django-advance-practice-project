from django.test import TestCase
from authentication.models import User, Appointment, Payment
from django.contrib.contenttypes.models import ContentType
from top_doctor.models import TopDoctor
from datetime import date, time

class TopDoctorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01700000000", password="password123")
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designation="Cardiologist",
            years_of_experience=10
        )

    def test_top_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(str(self.doctor), "Dr. Smith")

    def test_top_appointment_creation(self):
        appointment = Appointment.objects.create(
            user=self.user,
            content_type=ContentType.objects.get_for_model(TopDoctor),
            object_id=self.doctor.id,
            patient_name="John Doe",
            patient_phone="01800000000",
            appointment_date=date.today(),
            appointment_time=time(10, 0)
        )
        self.assertEqual(appointment.service_type, "top")
        self.assertEqual(str(appointment), f"Top Appointment for John Doe with {self.doctor.name}")

    def test_top_payment_creation(self):
        appointment = Appointment.objects.create(
            user=self.user,
            content_type=ContentType.objects.get_for_model(TopDoctor),
            object_id=self.doctor.id,
            patient_name="John Doe",
            patient_phone="01800000000",
            appointment_date=date.today(),
            appointment_time=time(10, 0)
        )
        payment = Payment.objects.create(
            appointment=appointment,
            method="bkash",
            amount=500.00,
            transaction_id="TXN123456"
        )
        self.assertEqual(payment.transaction_id, "TXN123456")
        self.assertEqual(str(payment), f"Payment for Appointment {appointment.id} - pending")
