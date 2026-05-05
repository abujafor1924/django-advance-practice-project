from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from top_doctor.models import TopDoctor, Booking, Payment
from top_doctor.serializers import TopDoctorSerializer, BookingSerializer, PaymentSerializer
from datetime import date, time

User = get_user_model()

class TopDoctorSerializerTest(TestCase):
    def setUp(self):
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        self.image = SimpleUploadedFile('test_image.gif', image_content, content_type='image/gif')
        self.doctor_data = {
            "name": "Dr. Smith",
            "designations": "Cardiologist",
            "experience": "10 years",
            "image": self.image
        }

    def test_top_doctor_serializer(self):
        serializer = TopDoctorSerializer(data=self.doctor_data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())

class BookingSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01700000000", password="password123")
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designations="Cardiologist",
            experience="10 years"
        )
        self.booking_data = {
            "doctor": self.doctor.id,
            "patient_name": "John Doe",
            "patient_phone": "01800000000",
            "appointment_date": str(date.today()),
            "appointment_time": "10:00:00"
        }

    def test_booking_serializer(self):
        serializer = BookingSerializer(data=self.booking_data)
        self.assertTrue(serializer.is_valid())

class PaymentSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01700000000", password="password123")
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designations="Cardiologist",
            experience="10 years"
        )
        self.booking = Booking.objects.create(
            doctor=self.doctor,
            user=self.user,
            patient_name="John Doe",
            patient_phone="01800000000",
            appointment_date=date.today(),
            appointment_time=time(10, 0)
        )
        self.payment_data = {
            "booking": self.booking.id,
            "payment_method": "bkash",
            "transaction_id": "TXN123456",
            "amount": 500.00
        }

    def test_payment_serializer(self):
        serializer = PaymentSerializer(data=self.payment_data)
        self.assertTrue(serializer.is_valid())
