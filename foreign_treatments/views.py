from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Country, Hospital, HospitalDetail
from .serializers import CountrySerializer, HospitalSerializer, HospitalDetailSerializer

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]

class CountryRetrieveView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]

class HospitalListView(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [AllowAny]

class HospitalRetrieveView(generics.RetrieveAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [AllowAny]

class CountryHospitalListView(generics.ListAPIView):
    queryset = Hospital.objects.none()
    serializer_class = HospitalSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Hospital.objects.none()
        
        country_id = self.kwargs.get('pk')
        if not country_id:
             return Hospital.objects.none()
             
        return Hospital.objects.filter(country_id=country_id)

class HospitalDetailRetrieveView(generics.RetrieveAPIView):
    queryset = HospitalDetail.objects.all()
    serializer_class = HospitalDetailSerializer
    lookup_field = 'hospital_id'
    permission_classes = [AllowAny]
