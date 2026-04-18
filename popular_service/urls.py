from django.urls import path
from .views import (
    ServiceCategoryListView, SubCategoryListView, DoctorListView,
    DoctorDetailView, BookingCreateView, PaymentCreateView
)

urlpatterns = [
    # Category APIs
    path('categories/', ServiceCategoryListView.as_view(), name='category-list'),
    path('subcategories/', SubCategoryListView.as_view(), name='subcategory-list'),

    # Doctor APIs
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Booking & Payment APIs
    path('bookings/', BookingCreateView.as_view(), name='booking-create'),
    path('payments/', PaymentCreateView.as_view(), name='payment-submit'),
]
