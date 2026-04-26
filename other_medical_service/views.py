from rest_framework import generics
from .models import MedicalServiceCategory, MedicalServiceDoctor
from .serializers import MedicalServiceCategorySerializer, MedicalServiceDoctorSerializer

class MedicalServiceCategoryListCreateView(generics.ListCreateAPIView):
    queryset = MedicalServiceCategory.objects.all()
    serializer_class = MedicalServiceCategorySerializer

class MedicalServiceCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalServiceCategory.objects.all()
    serializer_class = MedicalServiceCategorySerializer

class MedicalServiceDoctorListCreateView(generics.ListCreateAPIView):
    queryset = MedicalServiceDoctor.objects.all()
    serializer_class = MedicalServiceDoctorSerializer

class MedicalServiceDoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalServiceDoctor.objects.all()
    serializer_class = MedicalServiceDoctorSerializer
