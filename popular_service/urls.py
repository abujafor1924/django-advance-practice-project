from django.urls import path
from .views import (
    ServiceCategoryListView, SubCategoryListView, DoctorListView,
    DoctorDetailView,
    # Dashboard Views
    DoctorDashboardListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView
)

urlpatterns = [
    # Category APIs
    path('categories/', ServiceCategoryListView.as_view(), name='category-list'),
    path('subcategories/', SubCategoryListView.as_view(), name='subcategory-list'),

    # Doctor APIs
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Custom Dashboard URLs
    path('dashboard/', DoctorDashboardListView.as_view(), name='doctor-dashboard'),
    path('dashboard/add/', DoctorCreateView.as_view(), name='doctor-add'),
    path('dashboard/edit/<int:pk>/', DoctorUpdateView.as_view(), name='doctor-edit'),
    path('dashboard/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor-delete'),
]
