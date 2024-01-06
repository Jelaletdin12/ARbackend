import time

from django.db import models
from django.utils import timezone
# Create your models here.



class Profiller(models.Model):
    Profiliň_ady = models.CharField(max_length=50,)
    Surat = models.ImageField(upload_to='profiller', default='')
    Salgy = models.CharField(max_length=100, default='')
    Maglumat = models.TextField(default='')
    Tel_belgiler = models.CharField(max_length=100)
    Mail = models.EmailField(max_length=250, default='')
    Instagram = models.URLField(max_length=100, default='')
    createdAt = models.DateTimeField(default=timezone.now())

def __str__(self):
    return self.Profiliň_ady

def get_Tel_belgiler(self):
    return self.Tel_belgiler.split(',')

def set_Tel_belgiler(self, numbers):
    self.Tel_belgiler = ','.join(numbers)

class ProfileImage(models.Model):
    image = models.ImageField(upload_to='prolife-images/')
    profile = models.ForeignKey(Profiller, on_delete=models.CASCADE, related_name='images')

class Meta:
    ordering = ['-createdAt']



