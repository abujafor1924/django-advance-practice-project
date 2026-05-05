from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import TopDoctor, Booking, Payment
from .serializers import TopDoctorSerializer, BookingSerializer, PaymentSerializer, BookingDetailSerializer

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
