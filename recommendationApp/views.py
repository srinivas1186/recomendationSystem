from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.conf import settings
import subprocess
from subprocess import check_output
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', { 'videos':videos })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# logout
def userLogout(request):
    logout(request)
    return redirect('index')

# get video
@login_required
def getVideo(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES or None)
        if form.is_valid():
            temp  = form.save(commit=False)
            temp.created_by = request.user
            print(temp['videofile'])
            file_path = temp['videofile']['path']
            file_name = temp['videofile']['name']

            temp.thumbnail = file_name+'.jpg'
            check_output(f'ffmpeg  -itsoffset -4  -i {file_path} -vcodec mjpeg -vframes 1 -an -f rawvideo -s 320x240 {temp.thumbnail}', shell=True)
            temp.save()
            form.save_m2m()
            return redirect('home')
        else:
            return render(request, 'video.html', {'form': form})
    form = VideoForm()
    return render(request, 'video.html', {'form': form})
    

# add video
@login_required
def addVideo(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest('Invalid request')
# delete video
@login_required
def delVideo(request):
    if request.method == "DELETE":
        pass
    else:
        return HttpResponseBadRequest('Invalid request')
