from django.db import models

# Create your models here.
class tazelikler(models.Model):
    Tazeligiň_ady = models.CharField(max_length=250)
    Tazeligiň_maglumaty = models.TextField(default='')
    Tazeligiň_suraty = models.ImageField(upload_to='bannerler/')