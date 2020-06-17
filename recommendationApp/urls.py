from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name="index.html") , name='login'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name="index.html") , name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/',views.home, name='home'),
    path('logout/',views.userLogout,name='logout'),
    path('video/',views.getVideo),
    path('video/add/',views.addVideo),
    path('video/delete/',views.delVideo),
    path('generateThumbnail/',views.generateImages),
    path('play/addView/',views.addViewAndHistory),
    path(r'play/<id>',views.playVideo)
]