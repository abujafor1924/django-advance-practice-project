from django.urls import path
from .views import (
    QuoteWiserdListView, 
    QuoteWiserdDetailView, 
    NotificationListView, 
    NotificationMarkReadView
)

urlpatterns = [
    path('quote-wiserd/', QuoteWiserdListView.as_view(), name='quote-wiserd-list'),
    path('quote-wiserd/<int:pk>/', QuoteWiserdDetailView.as_view(), name='quote-wiserd-detail'),
    path('my-notifications/', NotificationListView.as_view(), name='notification-list'),
    path('my-notifications/<int:pk>/read/', NotificationMarkReadView.as_view(), name='notification-read'),
]
