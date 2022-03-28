from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path("", views.home, name = "home"),
    path("", views.upload, name = "upload"),
    path('', views.home),
    path('about', views.about)
]