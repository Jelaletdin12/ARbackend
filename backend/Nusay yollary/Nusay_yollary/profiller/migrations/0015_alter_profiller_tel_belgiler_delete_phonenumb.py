# Generated by Django 4.2.7 on 2023-12-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiller', '0014_phonenumb_delete_tel_belgiler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiller',
            name='Tel_belgiler',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='PhoneNumb',
        ),
    ]
