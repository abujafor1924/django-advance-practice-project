from django.urls import path
from .views import (
    RecordDocumentsCreateView, RecordDocumentsDetailView, RecordDocumentsListView, RegistrationView, LoginView,
    ProfileView, ResetPasswordView, LogoutView,
    UserAppointmentListView, AppointmentCreateView,
    UserServiceRecordView, PaymentCreateView
)

app_name = 'authentication'

urlpatterns = [
    #this is authentication urls for the application
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Appointment and Record URLs
    path('appointments/', UserAppointmentListView.as_view(), name='user-appointments'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='create-appointment'),
    path('service-records/', UserServiceRecordView.as_view(), name='service-records'),
    path('payments/submit/', PaymentCreateView.as_view(), name='payment-submit'),
    
    
    #record documents urls
    path('record-documents/', RecordDocumentsListView.as_view(), name='record-documents-list'),
    path('record-documents/create/', RecordDocumentsCreateView.as_view(), name='record-documents-create'),
    path('record-documents/<int:pk>/', RecordDocumentsDetailView.as_view(), name='record-documents-detail'),
    # path('record-documents/<int:pk>/delete/', RecordDocumentsDeleteView.as_view(), name='record-documents-delete'),
]
