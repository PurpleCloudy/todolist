from django.contrib import admin
from django.urls import path, include
from main.views import choosing_diff, list_of_tasks, simpletask_view

urlpatterns = [
    path('choosing/', choosing_diff, name='choosing'),
    path('creating_simple/', simpletask_view, name='simple_task'), 
    path('today/', list_of_tasks, name='task_list'),
    # path('', full_list, name="full_list"),
    # path('creating_complex/', complex_task, name='complex_task'),
]