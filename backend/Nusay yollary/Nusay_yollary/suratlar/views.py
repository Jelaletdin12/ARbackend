from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import suratlar
from .serializers import suratlarSerializer

class suratlarList(generics.ListAPIView):
    queryset = suratlar.objects.all()
    serializer_class = suratlarSerializer
