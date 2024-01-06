# Generated by Django 4.2.7 on 2023-12-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiller',
            name='Kontakt_maglumaty',
        ),
        migrations.RemoveField(
            model_name='profiller',
            name='Sosial_ulgam',
        ),
        migrations.RemoveField(
            model_name='profiller',
            name='Имя_профиля',
        ),
        migrations.AddField(
            model_name='profiller',
            name='Instagram',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profiller',
            name='Mail',
            field=models.EmailField(default='', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='profiller',
            name='Salgy',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='maglumatlar',
        ),
        migrations.DeleteModel(
            name='Sos_maglumat',
        ),
    ]