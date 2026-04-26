from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.MedicalServiceCategoryListCreateView.as_view(), name="medical-category-list"),
    path("categories/<int:pk>/", views.MedicalServiceCategoryRetrieveUpdateDestroyView.as_view(), name="medical-category-detail"),
    path("doctors/", views.MedicalServiceDoctorListCreateView.as_view(), name="medical-doctor-list"),
    path("doctors/<int:pk>/", views.MedicalServiceDoctorRetrieveUpdateDestroyView.as_view(), name="medical-doctor-detail"),
]
