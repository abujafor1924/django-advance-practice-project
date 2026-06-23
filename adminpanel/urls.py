from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminRecordDocumentsViewSet, AdminUserViewSet, AdminAppointmentViewSet, AdminPaymentViewSet

router = DefaultRouter()
router.register(r'users', AdminUserViewSet, basename='admin-users')
router.register(r'appointments', AdminAppointmentViewSet, basename='admin-appointments')
router.register(r'payments', AdminPaymentViewSet, basename='admin-payments')
router.register(r'record-documents', AdminRecordDocumentsViewSet, basename='admin-record-documents')

app_name = 'adminpanel'

urlpatterns = [
    path('', include(router.urls)),
]
