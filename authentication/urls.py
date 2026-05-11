from django.urls import path
from .views import (
    RegistrationView, LoginView,
    ProfileView, ResetPasswordView, LogoutView,
    UserAppointmentListView, AppointmentCreateView,
    UserServiceRecordView
)

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
]
