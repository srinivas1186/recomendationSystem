from django import forms
from django.forms import ModelForm
from .models import *

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['name','videofile','description']

