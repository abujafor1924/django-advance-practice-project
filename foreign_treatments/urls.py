from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.CountryListView.as_view(), name='country-list'),
    path('countries/<int:pk>/', views.CountryRetrieveView.as_view(), name='country-detail'),
    path('countries/<int:pk>/hospitals/', views.CountryHospitalListView.as_view(), name='country-hospitals'),
    path('hospitals/', views.HospitalListView.as_view(), name='hospital-list'),
    path('hospitals/<int:pk>/', views.HospitalRetrieveView.as_view(), name='hospital-detail'),
    path('hospital-details/<int:hospital_id>/', views.HospitalDetailRetrieveView.as_view(), name='hospital-detail-info'),
]
