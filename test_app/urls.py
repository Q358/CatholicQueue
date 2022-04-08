from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path("", views.home, name = "home"),
    path('chat', views.chat, name = "chat"),
    path('img', views.img),
    path('about', views.about),
    path('.well-known/acme-challenge/h0CofNTCyRTv8kNXJPEeoz91zh_S9MhFJLu8gHqYQ0I', views.acme)
] 