from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet, AdminAppointmentViewSet, AdminPaymentViewSet

router = DefaultRouter()
router.register(r'users', AdminUserViewSet, basename='admin-users')
router.register(r'appointments', AdminAppointmentViewSet, basename='admin-appointments')
router.register(r'payments', AdminPaymentViewSet, basename='admin-payments')

app_name = 'adminpanel'

urlpatterns = [
    path('', include(router.urls)),
]
