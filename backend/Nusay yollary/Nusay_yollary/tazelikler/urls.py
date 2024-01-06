from django.urls import path
from .views import tazeliklerList, tazelikDetay

urlpatterns = [
    path('api/tazelikler/', tazeliklerList.as_view(), name='tazelikler-list'),
    path('api/tazelikler/<int:pk>/', tazelikDetay.as_view(), name='tazelik-detay'),
    # Add other URL patterns as needed
]
