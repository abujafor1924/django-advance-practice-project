from django.urls import path
from .views import (
    RegistrationView, LoginView,
    ProfileView, ResetPasswordView, LogoutView
)

urlpatterns = [
    #this is authentication urls for the application
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
