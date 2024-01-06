from django.urls import path
from .views import suratlarList

urlpatterns = [
    path('api/suratlar/', suratlarList.as_view(), name='tazelikler-list'),
    # Add other URL patterns as needed
]