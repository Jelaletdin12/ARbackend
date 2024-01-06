from django.urls import path
from .views import BannerlerList

urlpatterns = [
    path('api/bannerler/', BannerlerList.as_view(), name='bannerler-list'),
    # Add other URL patterns as needed
]