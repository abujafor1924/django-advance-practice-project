from django.urls import path
from .views import (
    AccessoryCategoryListView,
    MedicalAccessoryListView,
    MedicalAccessoryDetailView
)

urlpatterns = [
    path('categories/', AccessoryCategoryListView.as_view(), name='category-list'),
    path('accessories/', MedicalAccessoryListView.as_view(), name='accessory-list'),
    path('accessories/<int:pk>/', MedicalAccessoryDetailView.as_view(), name='accessory-detail'),
]
