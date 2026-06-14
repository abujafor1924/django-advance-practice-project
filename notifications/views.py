from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import QuoteWiserd, Notification
from .serializers import QuoteWiserdSerializer, NotificationSerializer

class QuoteWiserdListView(generics.ListAPIView):
    """
    Returns a list of all QuoteWiserd notifications.
    """
    queryset = QuoteWiserd.objects.all()
    serializer_class = QuoteWiserdSerializer
    permission_classes = [AllowAny]

class QuoteWiserdDetailView(generics.RetrieveAPIView):
    """
    Returns a specific QuoteWiserd notification.
    """
    queryset = QuoteWiserd.objects.all()
    serializer_class = QuoteWiserdSerializer
    permission_classes = [AllowAny]

class NotificationListView(generics.ListAPIView):
    """
    Returns a list of notifications for the authenticated user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class NotificationMarkReadView(generics.UpdateAPIView):
    """
    Marks a notification as read.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response(status=status.HTTP_200_OK)
