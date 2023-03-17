from django.contrib import admin
from django.urls import path, include
from main.views import choosing_diff, list_of_tasks, simple_task, complex_task, full_list

urlpatterns = [
    path('choosing/', choosing_diff, name='choosing'),
    path('creating_simple/', simple_task, name='simple_task'), 
    path('today/', list_of_tasks, name='task_list'),
    path('', full_list, name="full_list"),
    path('creating_complex/', complex_task, name='complex_task'),
]