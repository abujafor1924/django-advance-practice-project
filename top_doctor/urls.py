from django.urls import path
from .views import TopDoctorListView, BookingCreateView, PaymentCreateView, UserBookingListView

urlpatterns = [
    path('doctors/', TopDoctorListView.as_view(), name='top-doctor-list'),
    path('bookings/', BookingCreateView.as_view(), name='top-doctor-booking-create'),
    path('my-bookings/', UserBookingListView.as_view(), name='top-doctor-user-bookings'),
    path('payments/', PaymentCreateView.as_view(), name='top-doctor-payment-create'),
]
