from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem
# Create your views here.

def runsrv(request):
    return render(request, 'home.html')


def todos(request):
    items = ToDoItem.objects.all()
    return render(request, 'todos.html', {'todos': items})