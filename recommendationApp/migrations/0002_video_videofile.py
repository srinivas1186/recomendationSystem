# Generated by Django 3.0.6 on 2020-05-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='videofile',
            field=models.FileField(default='/', upload_to='media/'),
            preserve_default=False,
        ),
    ]
