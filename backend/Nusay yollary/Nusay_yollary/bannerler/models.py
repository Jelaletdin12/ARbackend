from django.db import models


# Create your models here.



class Bannerler(models.Model):
    Surat = models.ImageField(upload_to='banner', default='')
    Link = models.URLField(max_length=100, default='')




