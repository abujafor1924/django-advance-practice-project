from django.urls import path
from .views import (
    SpecialDoctorListView, 
    SpecialDoctorDetailView,
    SpecialBookingCreateView,
    SpecialBookingListView,
    SpecialPaymentCreateView,
    # Dashboard Views
    SpecialDoctorDashboardListView, SpecialDoctorCreateView, SpecialDoctorUpdateView, SpecialDoctorDeleteView
)

urlpatterns = [
    path('doctors/', SpecialDoctorListView.as_view(), name='specialdoctor-list'),
    path('doctors/<int:pk>/', SpecialDoctorDetailView.as_view(), name='specialdoctor-detail'),
    path('bookings/', SpecialBookingListView.as_view(), name='special-booking-list'),
    path('bookings/create/', SpecialBookingCreateView.as_view(), name='special-booking-create'),
    path('payments/', SpecialPaymentCreateView.as_view(), name='special-payment-create'),

    # Custom Dashboard URLs
    path('dashboard/', SpecialDoctorDashboardListView.as_view(), name='special-doctor-dashboard'),
    path('dashboard/add/', SpecialDoctorCreateView.as_view(), name='special-doctor-add'),
    path('dashboard/edit/<int:pk>/', SpecialDoctorUpdateView.as_view(), name='special-doctor-edit'),
    path('dashboard/delete/<int:pk>/', SpecialDoctorDeleteView.as_view(), name='special-doctor-delete'),
]
