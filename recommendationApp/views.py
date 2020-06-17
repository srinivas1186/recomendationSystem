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
import json
# Create your views here.

HOME_VIDEOS_COUNT = 10
HISTORIES_TO_CONSIDER = 10

def index(request):
    return redirect('/home')

@login_required
def home(request):
    videos = []
    interest_tags = set()
    history = History.objects.filter(uid=request.user.id).order_by('-created_on') [:HISTORIES_TO_CONSIDER]
    if history:
        for h in history:
            tags = h.vid.tags.all() #Getting tags of watched videos
            for tag in tags:
                interest_tags.add(tag.id)
        searched_videos = Video.objects.filter(tags__in= interest_tags).distinct()[:HOME_VIDEOS_COUNT]
        videos = [*searched_videos ]
        searched_videos  = [ video.id for video in searched_videos]
        if len(videos)!=10:
            more_videos = Video.objects.exclude(id__in=searched_videos).order_by('-views')[:( HOME_VIDEOS_COUNT - len(searched_videos) )]
            videos = [*videos,*more_videos]
    else:
        videos = Video.objects.all().order_by("-views")[:HOME_VIDEOS_COUNT]
    
    # Get videos he is interested in using tags of videos he watched and order by views

    return render(request, 'home.html', { 'videos':videos })

def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
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

def makeThumbnail(id):
    video = Video.objects.get(id=id)
    if not video:
        return
    name = video.videofile.name + '.jpg'
    path = video.videofile.path + '.jpg'
    c = f'ffmpeg  -itsoffset -4  -i {video.videofile.path} -vcodec mjpeg -vframes 1 -an -f rawvideo -s 320x240 {path} -y'
    s = c.split()
    print(s)
    check_output(c, shell=True)
    video.thumbnail = path
    video.save()

# get video
@login_required
def getVideo(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES or None)
        if form.is_valid():
            temp  = form.save(commit=False)

            tags = request.POST["id_tags"] or ''
            tags = set([t.strip().lower() for t in tags.split(',')])
            tagObjects = []
            for tag in tags:
                try:
                    t = Tag.objects.get(name = tag)
                except:
                    t = None
                if not t:
                    t = Tag(name = tag)
                    t.save()
                tagObjects.append(t)
            temp.created_by = request.user
            file_path = temp.videofile.path
            file_name = temp.videofile.name
            temp.thumbnail = file_name+'.jpg'
            temp.save()
            temp.tags.add(*tagObjects)
            # makeThumbnail(temp.id)
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


# Generate thumbnails for videos 

def generateImages(request):
    videos = Video.objects.all()
    for video in videos:
        name = video.videofile.name + '.jpg'
        path = video.videofile.path + '.jpg'
        c = f'ffmpeg  -itsoffset -4  -i {video.videofile.path} -vcodec mjpeg -vframes 1 -an -f rawvideo -s 320x240 {path} -y'
        s = c.split()
        print(s)
        subprocess.call(c, shell=True)
        video.thumbnail = path
        video.save()

    return JsonResponse({'message':'Done!'})

@login_required
def playVideo(request,id):
    video = Video.objects.get(id=id)
    return render(request,'play.html',{"video":video})


@login_required
def addViewAndHistory(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request")
    body = json.loads(request.body)

    video = Video.objects.get(id = body['id'])
    if not video:
        return HttpResponseBadRequest("Invalid video id")
    
    video.views = video.views + 1
    video.save()
    # Create history
    history = History(uid=request.user,vid=video)
    history.save()

    return JsonResponse({"message":"Added successfully"})