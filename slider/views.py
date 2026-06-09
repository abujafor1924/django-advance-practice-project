from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import SliderOne, SliderTwo
from .serializers import (
    SliderOneListSerializer, SliderOneDetailSerializer,
    SliderTwoListSerializer, SliderTwoDetailSerializer
)

# SliderOne Views (Read-only for everyone)
class SliderOneListView(generics.ListAPIView):
    """
    Returns a list of all images for Slider One.
    """
    queryset = SliderOne.objects.all()
    serializer_class = SliderOneListSerializer
    permission_classes = [AllowAny]

class SliderOneDetailView(generics.RetrieveAPIView):
    """
    Returns a specific image for Slider One with full details.
    """
    queryset = SliderOne.objects.all()
    serializer_class = SliderOneDetailSerializer
    permission_classes = [AllowAny]


# SliderTwo Views (Read-only for everyone)
class SliderTwoListView(generics.ListAPIView):
    """
    Returns a list of all images for Slider Two.
    """
    queryset = SliderTwo.objects.all()
    serializer_class = SliderTwoListSerializer
    permission_classes = [AllowAny]

class SliderTwoDetailView(generics.RetrieveAPIView):
    """
    Returns a specific image for Slider Two with full details.
    """
    queryset = SliderTwo.objects.all()
    serializer_class = SliderTwoDetailSerializer
    permission_classes = [AllowAny]
