from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('slider/', include('slider.urls')),
    path('foreign-treatments/', include('foreign_treatments.urls')),
    path('popular-service/', include('popular_service.urls')),
    path('other-medical-service/', include('other_medical_service.urls')),
    path('medical-accessories/', include('medical_accessories.urls')),
    path('top-doctor/', include('top_doctor.urls')),
]