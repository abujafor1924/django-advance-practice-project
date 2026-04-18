from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServiceCategory, SubCategory, Hospital, Doctor, Booking, Payment
from .serializers import (
    ServiceCategorySerializer, SubCategorySerializer,
    DoctorListSerializer, DoctorDetailSerializer, BookingCreateSerializer,
    BookingListSerializer, PaymentSerializer
)

class ServiceCategoryListView(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    pagination_class = None

class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = None

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.select_related('hospital', 'subcategory').all()
    serializer_class = DoctorListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subcategory', 'subcategory__category']

class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.select_related('hospital', 'subcategory').all()
    serializer_class = DoctorDetailSerializer

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        
        return Response({
            "booking_id": booking.id,
            "message": "Booking created successfully. Please complete the manual payment to confirm.",
            "payment_instructions": {
                "bkash": "01XXXXXXXXX",
                "nagad": "01XXXXXXXXX",
                "manual_info": "Please submit your transaction ID via the Payment API."
            }
        }, status=status.HTTP_201_CREATED)

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
