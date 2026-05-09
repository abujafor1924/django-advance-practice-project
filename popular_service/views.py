from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServiceCategory, SubCategory, Hospital, Doctor, Booking, Payment
from .serializers import (
    ServiceCategorySerializer, SubCategorySerializer,
    DoctorListSerializer, DoctorDetailSerializer, BookingCreateSerializer,
    BookingListSerializer, PaymentSerializer
)
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import DoctorForm

# REST API Views
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

# Custom Dashboard Views (Tailwind CSS)
class DoctorDashboardListView(ListView):
    model = Doctor
    template_name = 'popular_service/dashboard/doctor_list.html'
    context_object_name = 'doctors'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'popular_service/dashboard/doctor_form.html'
    success_url = reverse_lazy('doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Doctor added successfully!")
        return super().form_valid(form)

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'popular_service/dashboard/doctor_form.html'
    success_url = reverse_lazy('doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Doctor updated successfully!")
        return super().form_valid(form)

class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctor-dashboard')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Doctor deleted successfully!")
        return super().delete(request, *args, **kwargs)
