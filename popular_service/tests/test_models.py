from django.test import TestCase
from popular_service.models import ServiceCategory, SubCategory, Hospital, Doctor, Booking, Payment

class ModelTestCase(TestCase):
    def setUp(self):
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

    def test_booking_creation(self):
        booking = Booking.objects.create(
            doctor=self.doctor,
            patient_name="John Doe",
            phone="01911111111",
            date="2026-05-10",
            time="10:00:00"
        )
        self.assertEqual(str(booking), f"Booking for John Doe with {self.doctor.name}")
        self.assertEqual(booking.status, "pending")

    def test_payment_creation(self):
        booking = Booking.objects.create(
            doctor=self.doctor,
            patient_name="John Doe",
            phone="01911111111",
            date="2026-05-10",
            time="10:00:00"
        )
        payment = Payment.objects.create(
            booking=booking,
            transaction_id="TXN12345",
            payment_method="bkash"
        )
        self.assertEqual(str(payment), f"Payment for Booking {booking.id} - pending")
