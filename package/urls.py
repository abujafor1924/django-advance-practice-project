from django.urls import path
from .views import (
    CollaborationsCompanyListView, 
    CollaborationsCompanyRetrieveView,
    PackageListView, 
    PackageRetrieveView, 
    SocialMediaServiceListView, 
    SocialMediaServiceRetrieveView
)

urlpatterns = [
    path('collaborations/', CollaborationsCompanyListView.as_view(), name='collaborations-list'),
    path('collaborations/<int:pk>/', CollaborationsCompanyRetrieveView.as_view(), name='collaborations-detail'),
    path('packages/', PackageListView.as_view(), name='package-list'),
    path('packages/<int:pk>/', PackageRetrieveView.as_view(), name='package-detail'),
    path('social-media-services/', SocialMediaServiceListView.as_view(), name='social-media-services-list'),
    path('social-media-services/<int:pk>/', SocialMediaServiceRetrieveView.as_view(), name='social-media-services-detail'),
]
