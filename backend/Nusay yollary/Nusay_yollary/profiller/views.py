from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
# Create your views here.
from rest_framework import generics, viewsets
from .models import Profiller, ProfileImage
from .serializers import ProfillerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.utils.translation import get_language_from_request

class ProfillerList(viewsets.ReadOnlyModelViewSet):
    queryset = Profiller.objects.all()
    serializer_class = ProfillerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Profiliň_ady_tk', 'Profiliň_ady_en', 'Profiliň_ady_ru', 'Maglumat_tk', 'Maglumat_en', 'Maglumat_ru']


