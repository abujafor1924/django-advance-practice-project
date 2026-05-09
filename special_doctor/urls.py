from django.urls import path
from .views import (
    SpecialDoctorListView, 
    SpecialDoctorDetailView,
    SpecialBookingCreateView,
    SpecialBookingListView,
    SpecialPaymentCreateView
)

urlpatterns = [
    path('doctors/', SpecialDoctorListView.as_view(), name='specialdoctor-list'),
    path('doctors/<int:pk>/', SpecialDoctorDetailView.as_view(), name='specialdoctor-detail'),
    path('bookings/', SpecialBookingListView.as_view(), name='special-booking-list'),
    path('bookings/create/', SpecialBookingCreateView.as_view(), name='special-booking-create'),
    path('payments/', SpecialPaymentCreateView.as_view(), name='special-payment-create'),
]
