from django.db import models

# Create your models here.
class suratlar(models.Model):
    Suratlar = models.ImageField(upload_to='static/img/bannerler', default='')