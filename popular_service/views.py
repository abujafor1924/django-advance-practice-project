from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServiceCategory, SubCategory, Hospital, Doctor
from django.db.models import Case, When, Value, IntegerField, Q
from .serializers import (
    ServiceCategorySerializer, SubCategorySerializer,
    DoctorListSerializer, DoctorDetailSerializer
)
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import DoctorForm

# REST API Views
class ServiceCategoryListView(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    pagination_class = None

class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = None

class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subcategories', 'subcategories__category']

    def get_queryset(self):
        return Doctor.objects.select_related(
            'hospital'
        ).prefetch_related(
            'subcategories'
        ).annotate(
            priority=Case(

                # Associate Professor
                When(
                    name__iregex=r'associate\s*prof',
                    then=Value(2)
                ),

                # Assistant Professor
                When(
                    name__iregex=r'assistant\s*prof',
                    then=Value(3)
                ),

                # Full Professor
                When(
                    name__iregex=r'(^|[\s\.])prof(\.|essor)?',
                    then=Value(1)
                ),

                default=Value(4),
                output_field=IntegerField()
            )
        ).order_by('priority', '-id')

class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.select_related('hospital').prefetch_related('subcategories').all()
    serializer_class = DoctorDetailSerializer

# Custom Dashboard Views (Tailwind CSS)
class DoctorDashboardListView(ListView):
    model = Doctor
    template_name = 'popular_service/dashboard/doctor_list.html'
    context_object_name = 'doctors'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'popular_service/dashboard/doctor_form.html'
    success_url = reverse_lazy('doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Doctor added successfully!")
        return super().form_valid(form)

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'popular_service/dashboard/doctor_form.html'
    success_url = reverse_lazy('doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Doctor updated successfully!")
        return super().form_valid(form)

class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctor-dashboard')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Doctor deleted successfully!")
        return super().delete(request, *args, **kwargs)
