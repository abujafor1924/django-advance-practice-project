from django.urls import path
from .views import (
    TopDoctorListView,
    # Dashboard Views
    TopDoctorDashboardListView, TopDoctorCreateView, TopDoctorUpdateView, TopDoctorDeleteView
)

urlpatterns = [
    path('doctors/', TopDoctorListView.as_view(), name='top-doctor-list'),

    # Custom Dashboard URLs
    path('dashboard/', TopDoctorDashboardListView.as_view(), name='top-doctor-dashboard'),
    path('dashboard/add/', TopDoctorCreateView.as_view(), name='top-doctor-add'),
    path('dashboard/edit/<int:pk>/', TopDoctorUpdateView.as_view(), name='top-doctor-edit'),
    path('dashboard/delete/<int:pk>/', TopDoctorDeleteView.as_view(), name='top-doctor-delete'),
]
