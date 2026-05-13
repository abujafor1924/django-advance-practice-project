from django.urls import path
from .views import CollaborationsCompanyListView, PackageListView, PackageRetrieveView

urlpatterns = [
    path('collaborations/', CollaborationsCompanyListView.as_view(), name='collaborations-list'),
    path('packages/', PackageListView.as_view(), name='package-list'),
    path('packages/<int:pk>/', PackageRetrieveView.as_view(), name='package-detail'),
]
