from django.test import TestCase
from django.contrib.auth import get_user_model
from top_doctor.models import TopDoctor, Booking, Payment
from datetime import date, time

User = get_user_model()

class TopDoctorModelTest(TestCase):
    def setUp(self):
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designation="Cardiologist",
            years_of_experience=10
        )

    def test_top_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(str(self.doctor), "Dr. Smith")

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01700000000", password="password123")
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designation="Cardiologist",
            years_of_experience=10
        )
        self.booking = Booking.objects.create(
            doctor=self.doctor,
            user=self.user,
            patient_name="John Doe",
            patient_phone="01800000000",
            appointment_date=date.today(),
            appointment_time=time(10, 0)
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.patient_name, "John Doe")
        self.assertEqual(str(self.booking), f"Booking for John Doe with Dr. Smith")

class PaymentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01700000000", password="password123")
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designation="Cardiologist",
            years_of_experience=10
        )
        self.booking = Booking.objects.create(
            doctor=self.doctor,
            user=self.user,
            patient_name="John Doe",
            patient_phone="01800000000",
            appointment_date=date.today(),
            appointment_time=time(10, 0)
        )
        self.payment = Payment.objects.create(
            booking=self.booking,
            payment_method="bkash",
            amount=500.00,
            transaction_id="TXN123456"
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.transaction_id, "TXN123456")
        self.assertEqual(str(self.payment), f"Payment for Booking {self.booking.id} - pending")
