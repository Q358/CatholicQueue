from django.shortcuts import render

from gitFolder import test_app
#from django.http import HttpResponse
from .models import Hour
from django.core.files.storage import FileSystemStorage

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

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'test_app/upload.html', {file.url:file_url})
    return render(request, 'test_app/upload.html')


#def about(request):
   # return render(request, 'test_app/about.html', {'title': 'About'})

