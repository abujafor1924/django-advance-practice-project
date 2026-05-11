from django.urls import path
from .views import (
    SpecialDoctorListView, 
    SpecialDoctorDetailView,
    # Dashboard Views
    SpecialDoctorDashboardListView, SpecialDoctorCreateView, SpecialDoctorUpdateView, SpecialDoctorDeleteView
)

urlpatterns = [
    path('doctors/', SpecialDoctorListView.as_view(), name='specialdoctor-list'),
    path('doctors/<int:pk>/', SpecialDoctorDetailView.as_view(), name='specialdoctor-detail'),

    # Custom Dashboard URLs
    path('dashboard/', SpecialDoctorDashboardListView.as_view(), name='special-doctor-dashboard'),
    path('dashboard/add/', SpecialDoctorCreateView.as_view(), name='special-doctor-add'),
    path('dashboard/edit/<int:pk>/', SpecialDoctorUpdateView.as_view(), name='special-doctor-edit'),
    path('dashboard/delete/<int:pk>/', SpecialDoctorDeleteView.as_view(), name='special-doctor-delete'),
]
