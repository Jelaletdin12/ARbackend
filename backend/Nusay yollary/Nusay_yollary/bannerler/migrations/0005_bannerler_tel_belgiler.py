# Generated by Django 4.2.7 on 2023-12-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bannerler', '0004_bannerler_surat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerler',
            name='Tel_belgiler',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]