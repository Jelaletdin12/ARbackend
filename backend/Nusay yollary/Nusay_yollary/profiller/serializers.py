# serializers.py
from rest_framework import serializers
from .models import Profiller, ProfileImage


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ['id', 'image']



class ProfillerSerializer(serializers.ModelSerializer):
    images = ProfileImageSerializer(many=True, read_only=True)
    class Meta:
        model = Profiller
        fields = ['id', 'Profiliň_ady', 'Profiliň_ady_ru', 'Salgy', 'Tel_belgiler', 'Surat', 'Maglumat', 'Maglumat_ru', 'Maglumat_tk',  'Mail', 'Instagram', 'images']
