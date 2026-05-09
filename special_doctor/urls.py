from django.urls import path
from .views import (
    SpecialCategoryListView, 
    SpecialHospitalListView, 
    SpecialDoctorListView, 
    SpecialDoctorDetailView,
    SpecialBookingCreateView,
    SpecialBookingListView,
    SpecialPaymentCreateView
)

urlpatterns = [
    path('categories/', SpecialCategoryListView.as_view(), name='special-category-list'),
    path('hospitals/', SpecialHospitalListView.as_view(), name='special-hospital-list'),
    path('doctors/', SpecialDoctorListView.as_view(), name='specialdoctor-list'),
    path('doctors/<int:pk>/', SpecialDoctorDetailView.as_view(), name='specialdoctor-detail'),
    path('bookings/', SpecialBookingListView.as_view(), name='special-booking-list'),
    path('bookings/create/', SpecialBookingCreateView.as_view(), name='special-booking-create'),
    path('payments/', SpecialPaymentCreateView.as_view(), name='special-payment-create'),
]
