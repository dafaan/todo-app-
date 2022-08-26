from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    event = events.objects.all()
    context = {'event':event}
    return render(request, 'home.html', context)

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        print(title) 
        event = events.objects.create(title=title)
        event.save()
        return redirect('/')
    context={}
    return render(request, 'add.html', context)


def update(request, id):
    i = events.objects.get(id=id)
    a = i.title
    if request.method == 'POST':
        title = request.POST['title']
        i.title = title 
        i.save()
        return redirect('/')
    context = {'event':i, 'a':a}
    return render(request, 'update.html', context,)

def delete(request, id):
    i = get_object_or_404(events, id=id)
    i.delete()
    print(i)
    context = {}
    return redirect('/')
