# Generated by Django 4.2.7 on 2023-12-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiller', '0002_remove_profiller_kontakt_maglumaty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiller',
            name='Tel_belgiler',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
