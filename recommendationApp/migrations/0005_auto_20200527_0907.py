# Generated by Django 3.0.6 on 2020-05-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationApp', '0004_auto_20200527_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Video views'),
        ),
    ]
