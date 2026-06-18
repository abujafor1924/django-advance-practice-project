from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from authentication.models import User, Appointment, Payment
from .serializers import AdminUserSerializer, AdminAppointmentSerializer, AdminPaymentSerializer

@extend_schema_view(
    list=extend_schema(tags=['Admin Panel']),
    retrieve=extend_schema(tags=['Admin Panel']),
    create=extend_schema(tags=['Admin Panel']),
    update=extend_schema(tags=['Admin Panel']),
    partial_update=extend_schema(tags=['Admin Panel']),
    destroy=extend_schema(tags=['Admin Panel']),
)
class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = AdminUserSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'is_staff', 'is_verified']
    search_fields = ['phone_number', 'name', 'email', 'district']
    ordering_fields = ['created_at', 'name']

@extend_schema_view(
    list=extend_schema(tags=['Admin Panel']),
    retrieve=extend_schema(tags=['Admin Panel']),
    create=extend_schema(tags=['Admin Panel']),
    update=extend_schema(tags=['Admin Panel']),
    partial_update=extend_schema(tags=['Admin Panel']),
    destroy=extend_schema(tags=['Admin Panel']),
)
class AdminAppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-created_at')
    serializer_class = AdminAppointmentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'service_type', 'appointment_date']
    search_fields = ['patient_name', 'patient_phone']
    ordering_fields = ['created_at', 'appointment_date', 'appointment_time']

@extend_schema_view(
    list=extend_schema(tags=['Admin Panel']),
    retrieve=extend_schema(tags=['Admin Panel']),
    create=extend_schema(tags=['Admin Panel']),
    update=extend_schema(tags=['Admin Panel']),
    partial_update=extend_schema(tags=['Admin Panel']),
    destroy=extend_schema(tags=['Admin Panel']),
)
class AdminPaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('-created_at')
    serializer_class = AdminPaymentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'method']
    search_fields = ['transaction_id', 'appointment__patient_name', 'appointment__patient_phone']
    ordering_fields = ['created_at', 'amount']
