from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import SpecialDoctor, SpecialBooking, SpecialPayment
from .serializers import (
    SpecialDoctorListSerializer, 
    SpecialDoctorDetailSerializer,
    SpecialBookingCreateSerializer,
    SpecialBookingListSerializer,
    SpecialPaymentSerializer
)

class SpecialDoctorListView(generics.ListAPIView):
    queryset = SpecialDoctor.objects.select_related('hospital', 'subcategory__category').all()
    serializer_class = SpecialDoctorListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['subcategory', 'subcategory__category', 'hospital']
    search_fields = ['name', 'designation']
    ordering_fields = ['years_of_experience', 'doctor_fees']

class SpecialDoctorDetailView(generics.RetrieveAPIView):
    queryset = SpecialDoctor.objects.all()
    serializer_class = SpecialDoctorDetailSerializer

class SpecialBookingCreateView(generics.CreateAPIView):
    queryset = SpecialBooking.objects.all()
    serializer_class = SpecialBookingCreateSerializer

class SpecialBookingListView(generics.ListAPIView):
    queryset = SpecialBooking.objects.all()
    serializer_class = SpecialBookingListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['created_at']

class SpecialPaymentCreateView(generics.CreateAPIView):
    queryset = SpecialPayment.objects.all()
    serializer_class = SpecialPaymentSerializer
