from django.urls import path
from . import views

app_name = 'foreign_treatments'

urlpatterns = [
    path('countries/', views.CountryListView.as_view(), name='country-list'),
    path('countries/<int:pk>/', views.CountryRetrieveView.as_view(), name='country-detail'),
    path('countries/<int:pk>/hospitals/', views.CountryHospitalListView.as_view(), name='country-hospitals'),
    path('hospitals/', views.HospitalListView.as_view(), name='hospital-list'),
    path('hospitals/<int:pk>/', views.HospitalRetrieveView.as_view(), name='hospital-detail'),
    path('hospital-details/<int:hospital_id>/', views.HospitalDetailRetrieveView.as_view(), name='hospital-detail-info'),
    path('bangladesh-hospitals/', views.BangladeshHospitalListView.as_view(), name='bangladesh-hospital-list'),
    path('bangladesh-hospitals/<int:pk>/', views.BangladeshHospitalRetrieveView.as_view(), name='bangladesh-hospital-detail'),
    path('international-guardian-hospitals/', views.InternationalGuardianHospitalListView.as_view(), name='international-guardian-hospital-list'),
    path('international-guardian-hospitals/<int:pk>/', views.InternationalGuardianHospitalRetrieveView.as_view(), name='international-guardian-hospital-detail'),
]
