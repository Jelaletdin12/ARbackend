# Generated by Django 4.2.7 on 2023-12-28 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiller', '0013_profiller_profiliň_ady_en_profiller_profiliň_ady_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumb2', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PhoneNumb2', to='profiller.profiller')),
            ],
        ),
        migrations.DeleteModel(
            name='Tel_belgiler',
        ),
    ]
