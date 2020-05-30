This django project is used to recommend videos based on previous history of the user logged in.


Requirements:
- Need Python(3.8+)
- Django version(3.0.6)
- Download ffmpeg (https://www.ffmpeg.org/download.html)
  ffmpeg is used to build thumbnails of videos added 

Ffmpeg installation for windows
https://www.wikihow.com/Install-FFmpeg-on-Windows

Ffmpeg installation for ubuntu
sudo apt install ffmpeg

Setup steps:

```
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage,py runserver

```