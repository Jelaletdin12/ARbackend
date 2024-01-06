# serializers.py
from rest_framework import serializers
from .models import suratlar

class suratlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = suratlar
        fields = '__all__'
