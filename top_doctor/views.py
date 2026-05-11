from rest_framework import generics, permissions
from .models import TopDoctor
from .serializers import TopDoctorSerializer
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import TopDoctorForm

class TopDoctorListView(generics.ListAPIView):
    queryset = TopDoctor.objects.all()
    serializer_class = TopDoctorSerializer
    permission_classes = [permissions.AllowAny]

# Custom Dashboard Views (Tailwind CSS)
class TopDoctorDashboardListView(ListView):
    model = TopDoctor
    template_name = 'top_doctor/dashboard/doctor_list.html'
    context_object_name = 'doctors'

class TopDoctorCreateView(CreateView):
    model = TopDoctor
    form_class = TopDoctorForm
    template_name = 'top_doctor/dashboard/doctor_form.html'
    success_url = reverse_lazy('top-doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Top Doctor added successfully!")
        return super().form_valid(form)

class TopDoctorUpdateView(UpdateView):
    model = TopDoctor
    form_class = TopDoctorForm
    template_name = 'top_doctor/dashboard/doctor_form.html'
    success_url = reverse_lazy('top-doctor-dashboard')

    def form_valid(self, form):
        messages.success(self.request, "Top Doctor updated successfully!")
        return super().form_valid(form)

class TopDoctorDeleteView(DeleteView):
    model = TopDoctor
    success_url = reverse_lazy('top-doctor-dashboard')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Top Doctor deleted successfully!")
        return super().delete(request, *args, **kwargs)
