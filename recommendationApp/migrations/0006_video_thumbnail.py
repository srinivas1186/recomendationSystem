# Generated by Django 3.0.6 on 2020-05-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationApp', '0005_auto_20200527_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default='', height_field=200, upload_to='', verbose_name='thumnail', width_field=300),
            preserve_default=False,
        ),
    ]
