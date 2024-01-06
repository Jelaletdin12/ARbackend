from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
# Create your views here.
from rest_framework import generics
from .models import tazelikler
from .serializers import tazeliklerSerializer

class tazeliklerList(generics.ListAPIView):
    queryset = tazelikler.objects.all()
    serializer_class = tazeliklerSerializer


class tazelikDetay(RetrieveAPIView):
    queryset = tazelikler.objects.all()
    serializer_class = tazeliklerSerializer