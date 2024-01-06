# Generated by Django 4.2.7 on 2023-12-26 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiller', '0009_harytsurat_alter_profiller_profiliň_ady_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prolife-images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='profiller',
            name='Haryt_suratlar',
        ),
        migrations.AlterField(
            model_name='profiller',
            name='Profiliň_ady',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='HarytSurat',
        ),
        migrations.AddField(
            model_name='profileimage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiller.profiller'),
        ),
    ]
