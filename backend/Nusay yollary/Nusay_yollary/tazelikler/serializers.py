# serializers.py
from rest_framework import serializers
from .models import tazelikler

class tazeliklerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tazelikler
        fields = ['id', 'Tazeligiň_ady', 'Tazeligiň_maglumaty', 'Tazeligiň_ady_tk', 'Tazeligiň_maglumaty_ru', 'Tazeligiň_suraty']
