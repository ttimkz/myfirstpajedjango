from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('firstpage/', views.runsrv, name='hello'),
    path('todos/', views.todos, name='todos')
]
