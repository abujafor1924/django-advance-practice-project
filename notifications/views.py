from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import QuoteWiserd
from .serializers import QuoteWiserdSerializer

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
