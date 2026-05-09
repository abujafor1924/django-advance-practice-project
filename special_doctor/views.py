from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import SpecialCategory, SpecialHospital, SpecialDoctor, SpecialBooking, SpecialPayment
from .serializers import (
    SpecialCategorySerializer, 
    SpecialHospitalSerializer, 
    SpecialDoctorListSerializer, 
    SpecialDoctorDetailSerializer,
    SpecialBookingCreateSerializer,
    SpecialBookingListSerializer,
    SpecialPaymentSerializer
)

class SpecialCategoryListView(generics.ListAPIView):
    queryset = SpecialCategory.objects.all()
    serializer_class = SpecialCategorySerializer

class SpecialHospitalListView(generics.ListAPIView):
    queryset = SpecialHospital.objects.all()
    serializer_class = SpecialHospitalSerializer

class SpecialDoctorListView(generics.ListAPIView):
    queryset = SpecialDoctor.objects.all()
    serializer_class = SpecialDoctorListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'hospital']
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
