# Generated by Django 3.0.6 on 2020-05-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationApp', '0008_auto_20200530_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='recommendationApp.Tag'),
        ),
    ]