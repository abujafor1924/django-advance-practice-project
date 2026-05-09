from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import TopDoctor, Booking, Payment
from .serializers import TopDoctorSerializer, BookingSerializer, PaymentSerializer, BookingDetailSerializer
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import TopDoctorForm

class TopDoctorListView(generics.ListAPIView):
    queryset = TopDoctor.objects.all()
    serializer_class = TopDoctorSerializer
    permission_classes = [permissions.AllowAny]

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        booking_id = request.data.get('booking')
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found or does not belong to user"}, status=status.HTTP_404_NOT_FOUND)
        
        return super().create(request, *args, **kwargs)

class UserBookingListView(generics.ListAPIView):
    serializer_class = BookingDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# Custom Dashboard Views (Tailwind CSS)
class TopDoctorDashboardListView(ListView):
    model = TopDoctor
    template_name = 'top_doctor/dashboard/doctor_list.html'
    context_object_name = 'doctors'

class TopDoctorCreateView(CreateView):
    model = TopDoctor
    form_class = TopDoctorForm
    template_name = 'top_doctor/dashboard/doctor_form.html'
    success_url = reverse_lazy('top-doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Top Doctor added successfully!")
        return super().form_valid(form)

class TopDoctorUpdateView(UpdateView):
    model = TopDoctor
    form_class = TopDoctorForm
    template_name = 'top_doctor/dashboard/doctor_form.html'
    success_url = reverse_lazy('top-doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Top Doctor updated successfully!")
        return super().form_valid(form)

class TopDoctorDeleteView(DeleteView):
    model = TopDoctor
    success_url = reverse_lazy('top-doctor-dashboard')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Top Doctor deleted successfully!")
        return super().delete(request, *args, **kwargs)
