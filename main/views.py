from django.shortcuts import render, redirect
from .forms import ChoosingTaskModelForm, SimpleTaskModelForm, ComplexTaskModelForm
from .models import Task
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime

# Create your views here.
def choosing_diff(request):
    if request.method == 'POST':
        form = ChoosingTaskModelForm(request.POST or None)
        if form.is_valid():
            obj = Task
            diff = form.cleaned_data.get('difficulty')
            date = form.cleaned_data.get('date')
            obj.difficulty = diff
            obj.date = date
            obj.save()
            return redirect('simple_task')
    else:
        form = ChoosingTaskModelForm()
    return render(request, 'main/difficulty.html', {'form':form}) 

def simpletask_view(request, *args, **kwargs):
    print(args)
    return render(request, 'main/simple_task.html')

def list_of_tasks(request, *args, **kwargs):
    current_date = datetime.now()
    qs = Task.objects.filter(month=current_date.month, day=current_date.day)
    return render(request, 'homepage.html', {'qs':qs})





