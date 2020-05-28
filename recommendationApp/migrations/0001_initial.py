# Generated by Django 3.0.6 on 2020-05-25 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Tag Id')),
                ('name', models.TextField(verbose_name='Tag Name')),
                ('description', models.TextField(default='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Video Id')),
                ('name', models.TextField(verbose_name='Video Name')),
                ('path', models.TextField(verbose_name='File Path')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(verbose_name='Video views')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='recommendationApp.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_views', models.IntegerField(default=0, verbose_name='Video views')),
                ('interests', models.ManyToManyField(to='recommendationApp.Tag')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendationApp.Video')),
            ],
        ),
    ]
