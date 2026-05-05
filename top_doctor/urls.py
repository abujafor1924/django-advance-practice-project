from django.urls import path
from .views import TopDoctorListView, BookingCreateView, PaymentCreateView, UserBookingListView

urlpatterns = [
    path('doctors/', TopDoctorListView.as_view(), name='doctor-list'),
    path('bookings/', BookingCreateView.as_view(), name='booking-create'),
    path('my-bookings/', UserBookingListView.as_view(), name='user-bookings'),
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
]
