from django.shortcuts import render
#from django.http import HttpResponse
from .models import Hour

# Create your views here.
# request -> response - request handler

test = {
    'lineLength': 10,
    'busynessLevel': "Busy"
}

def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', { 'name': 'People' })

def home(request):
    context = {
        'title': 'CatholicQueue | Home',
        'currentHour': Hour.objects.filter(isCurrent = True).first(),
        'hours': Hour.objects.all()
    }
    return render(request, 'test_app/home.html', context)

def about(request):
    return render(request, 'test_app/about.html', {'title': 'About'})
