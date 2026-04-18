from django.urls import path
from .views import (
    SliderOneListView, SliderOneDetailView,
    SliderTwoListView, SliderTwoDetailView
)

urlpatterns = [
    # Slider One URLs
    path('slider-one/', SliderOneListView.as_view(), name='slider-one-list'),
    path('slider-one/<int:pk>/', SliderOneDetailView.as_view(), name='slider-one-detail'),

    # Slider Two URLs
    path('slider-two/', SliderTwoListView.as_view(), name='slider-two-list'),
    path('slider-two/<int:pk>/', SliderTwoDetailView.as_view(), name='slider-two-detail'),
]
