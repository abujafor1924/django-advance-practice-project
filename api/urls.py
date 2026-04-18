from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('slider/', include('slider.urls')),
    path('foreign-treatments/', include('foreign_treatments.urls')),
    path('popular-service/', include('popular_service.urls')),
]