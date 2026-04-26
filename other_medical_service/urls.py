from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.MedicalServiceCategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", views.MedicalServiceCategoryRetrieveUpdateDestroyView.as_view(), name="category-detail"),
    path("doctors/", views.MedicalServiceDoctorListCreateView.as_view(), name="doctor-list"),
    path("doctors/<int:pk>/", views.MedicalServiceDoctorRetrieveUpdateDestroyView.as_view(), name="doctor-detail"),
]
