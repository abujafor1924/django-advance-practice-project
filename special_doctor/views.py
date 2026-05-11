from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import SpecialDoctor
from .serializers import (
    SpecialDoctorListSerializer, 
    SpecialDoctorDetailSerializer
)
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import SpecialDoctorForm

class SpecialDoctorListView(generics.ListAPIView):
    queryset = SpecialDoctor.objects.select_related('hospital', 'subcategory__category').all()
    serializer_class = SpecialDoctorListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['subcategory', 'subcategory__category', 'hospital']
    search_fields = ['name', 'designation']
    ordering_fields = ['years_of_experience', 'doctor_fees']

class SpecialDoctorDetailView(generics.RetrieveAPIView):
    queryset = SpecialDoctor.objects.all()
    serializer_class = SpecialDoctorDetailSerializer

# Custom Dashboard Views (Tailwind CSS)
class SpecialDoctorDashboardListView(ListView):
    model = SpecialDoctor
    template_name = 'special_doctor/dashboard/doctor_list.html'
    context_object_name = 'doctors'

class SpecialDoctorCreateView(CreateView):
    model = SpecialDoctor
    form_class = SpecialDoctorForm
    template_name = 'special_doctor/dashboard/doctor_form.html'
    success_url = reverse_lazy('special-doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Special Doctor added successfully!")
        return super().form_valid(form)

class SpecialDoctorUpdateView(UpdateView):
    model = SpecialDoctor
    form_class = SpecialDoctorForm
    template_name = 'special_doctor/dashboard/doctor_form.html'
    success_url = reverse_lazy('special-doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Special Doctor updated successfully!")
        return super().form_valid(form)

class SpecialDoctorDeleteView(DeleteView):
    model = SpecialDoctor
    success_url = reverse_lazy('special-doctor-dashboard')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Special Doctor deleted successfully!")
        return super().delete(request, *args, **kwargs)
