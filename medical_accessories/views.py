from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import MedicalAccessory, AccessoryCategory
from .serializers import (
    MedicalAccessoryListSerializer, 
    MedicalAccessoryDetailSerializer,
    AccessoryCategorySerializer
)

class AccessoryCategoryListView(generics.ListAPIView):
    queryset = AccessoryCategory.objects.all()
    serializer_class = AccessoryCategorySerializer
    permission_classes = [AllowAny]

class MedicalAccessoryListView(generics.ListAPIView):
    queryset = MedicalAccessory.objects.all()
    serializer_class = MedicalAccessoryListSerializer
    permission_classes = [AllowAny]

class MedicalAccessoryDetailView(generics.RetrieveAPIView):
    queryset = MedicalAccessory.objects.all()
    serializer_class = MedicalAccessoryDetailSerializer
    permission_classes = [AllowAny]
