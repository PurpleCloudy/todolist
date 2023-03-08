from django.contrib import admin
from django.urls import path, include
from main.views import creating_task, list_of_tasks

urlpatterns = [
    path('creating/', creating_task), 
    path('today/', list_of_tasks, name='tasklist'),
]