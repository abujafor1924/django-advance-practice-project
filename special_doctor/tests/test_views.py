from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import SpecialCategory, SpecialHospital, SpecialDoctor, SpecialBooking, SpecialPayment

class SpecialDoctorViewSetTest(APITestCase):
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

    def test_get_special_doctor_list(self):
        url = reverse('specialdoctor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if one doctor is returned
        self.assertEqual(len(response.data['results']), 1)

    def test_get_special_doctor_detail(self):
        url = reverse('specialdoctor-detail', args=[self.doctor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Dr. Smith")

    def test_filter_doctors_by_category(self):
        url = reverse('specialdoctor-list')
        response = self.client.get(url, {'category': self.category.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        other_category = SpecialCategory.objects.create(name="Dermatology")
        response = self.client.get(url, {'category': other_category.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

class SpecialBookingViewSetTest(APITestCase):
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
        self.booking_data = {
            'doctor': self.doctor.id,
            'patient_name': 'John Doe',
            'phone': '1234567890',
            'date': '2026-05-20',
            'time': '10:00:00'
        }

    def test_create_booking(self):
        url = reverse('special-booking-create')
        response = self.client.post(url, self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SpecialBooking.objects.count(), 1)

    def test_get_booking_list(self):
        SpecialBooking.objects.create(**self.booking_data | {'doctor': self.doctor})
        url = reverse('special-booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

class SpecialPaymentViewSetTest(APITestCase):
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
        self.booking = SpecialBooking.objects.create(
            doctor=self.doctor,
            patient_name='John Doe',
            phone='1234567890',
            date='2026-05-20',
            time='10:00:00'
        )
        self.payment_data = {
            'booking': self.booking.id,
            'transaction_id': 'TXN12345',
            'payment_method': 'manual'
        }

    def test_create_payment(self):
        url = reverse('special-payment-create')
        response = self.client.post(url, self.payment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SpecialPayment.objects.count(), 1)
