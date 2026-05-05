from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from top_doctor.models import TopDoctor, Booking, Payment
from datetime import date, time

User = get_user_model()

class TopDoctorViewsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number="01700000000", password="password123")
        self.doctor = TopDoctor.objects.create(
            name="Dr. Smith",
            designations="Cardiologist",
            experience="10 years"
        )
        self.doctor_list_url = reverse('doctor-list')
        self.booking_create_url = reverse('booking-create')
        self.user_bookings_url = reverse('user-bookings')
        self.payment_create_url = reverse('payment-create')

    def test_get_doctor_list(self):
        response = self.client.get(self.doctor_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_booking_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "doctor": self.doctor.id,
            "patient_name": "John Doe",
            "patient_phone": "01800000000",
            "appointment_date": str(date.today()),
            "appointment_time": "10:00:00"
        }
        response = self.client.post(self.booking_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().user, self.user)

    def test_create_booking_unauthenticated(self):
        data = {
            "doctor": self.doctor.id,
            "patient_name": "John Doe",
            "patient_phone": "01800000000",
            "appointment_date": str(date.today()),
            "appointment_time": "10:00:00"
        }
        response = self.client.post(self.booking_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_payment_authenticated(self):
        self.client.force_authenticate(user=self.user)
        booking = Booking.objects.create(
            doctor=self.doctor,
            user=self.user,
            patient_name="John Doe",
            patient_phone="01800000000",
            appointment_date=date.today(),
            appointment_time=time(10, 0)
        )
        data = {
            "booking": booking.id,
            "payment_method": "bkash",
            "transaction_id": "TXN123456",
            "amount": 500.00
        }
        response = self.client.post(self.payment_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

    def test_get_user_bookings(self):
        self.client.force_authenticate(user=self.user)
        Booking.objects.create(
            doctor=self.doctor,
            user=self.user,
            patient_name="John Doe",
            patient_phone="01800000000",
            appointment_date=date.today(),
            appointment_time=time(10, 0)
        )
        response = self.client.get(self.user_bookings_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
