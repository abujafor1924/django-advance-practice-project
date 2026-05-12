from django.urls import path
from .views import QuoteWiserdListView, QuoteWiserdDetailView

urlpatterns = [
    path('quote-wiserd/', QuoteWiserdListView.as_view(), name='quote-wiserd-list'),
    path('quote-wiserd/<int:pk>/', QuoteWiserdDetailView.as_view(), name='quote-wiserd-detail'),
]
