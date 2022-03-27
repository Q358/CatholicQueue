from django.shortcuts import render
from django.http import HttpResponse
from .models import Hour

# Create your views here.
# request -> response - request handler

def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', { 'name': 'People' })

def home(request):
    context = {
        'busyness': Hour.objects.filter(isCurrent = True).first()
    }
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
