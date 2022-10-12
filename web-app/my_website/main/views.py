from django.shortcuts import render


# Create your views here.
from .models import Task, SomeInfo

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/main.html',{'title':'Main page','tasks': tasks})

def info(request):
    inf = SomeInfo.objects.all()
    return render(request, 'main/SomeInfo.html', {'title': 'Some Info', 'inf': inf})