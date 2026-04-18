from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import SliderOne, SliderTwo
from .serializers import SliderOneSerializer, SliderTwoSerializer

# SliderOne Views (Read-only for everyone)
class SliderOneListView(generics.ListAPIView):
    """
    Returns a list of all images for Slider One.
    """
    queryset = SliderOne.objects.all()
    serializer_class = SliderOneSerializer
    permission_classes = [AllowAny]

class SliderOneDetailView(generics.RetrieveAPIView):
    """
    Returns a specific image for Slider One.
    """
    queryset = SliderOne.objects.all()
    serializer_class = SliderOneSerializer
    permission_classes = [AllowAny]


# SliderTwo Views (Read-only for everyone)
class SliderTwoListView(generics.ListAPIView):
    """
    Returns a list of all images for Slider Two.
    """
    queryset = SliderTwo.objects.all()
    serializer_class = SliderTwoSerializer
    permission_classes = [AllowAny]

class SliderTwoDetailView(generics.RetrieveAPIView):
    """
    Returns a specific image for Slider Two.
    """
    queryset = SliderTwo.objects.all()
    serializer_class = SliderTwoSerializer
    permission_classes = [AllowAny]
