from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CollaborationsCompany, Package
from .serializers import CollaborationsCompanySerializer, PackageSerializer

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
