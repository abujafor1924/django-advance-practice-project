from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CollaborationsCompany, Package, SocialMediaService
from .serializers import CollaborationsCompanySerializer, PackageSerializer, SocialMediaServiceSerializer

class CollaborationsCompanyListView(generics.ListAPIView):
    queryset = CollaborationsCompany.objects.all()
    serializer_class = CollaborationsCompanySerializer
    permission_classes = [AllowAny]

class PackageListView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [AllowAny]

class PackageRetrieveView(generics.RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [AllowAny]

class SocialMediaServiceListView(generics.ListAPIView):
    queryset = SocialMediaService.objects.all()
    serializer_class = SocialMediaServiceSerializer
    permission_classes = [AllowAny]
