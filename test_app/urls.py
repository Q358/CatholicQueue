from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path("", views.home, name = "home"),
    path('upload', views.upload, name = "upload"),
    path('img', views.img),
    path('about', views.about)
] 