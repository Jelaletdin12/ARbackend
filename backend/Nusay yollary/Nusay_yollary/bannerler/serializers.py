# serializers.py
from rest_framework import serializers
from .models import Bannerler

class BannerlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bannerler
        fields = '__all__'
