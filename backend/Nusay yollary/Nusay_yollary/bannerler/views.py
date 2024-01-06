from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Bannerler
from .serializers import BannerlerSerializer

class BannerlerList(generics.ListAPIView):
    queryset = Bannerler.objects.all()
    serializer_class = BannerlerSerializer
