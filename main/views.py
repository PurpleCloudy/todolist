from django.shortcuts import render
from .forms import ComplexTaskModelForm
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.
def creating_task(request, *args, **kwargs):
    if request.method == "POST":
        form = ComplexTaskModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = ComplexTaskModelForm()
            return HttpResponseRedirect(reverse('tasklist'))
    form = ComplexTaskModelForm(request.POST or None)
    return render(request, 'forms.html', {'form':form})

def list_of_tasks(request, *args, **kwargs):
    current_date = datetime.now()
    qs = Task.objects.filter(month=current_date.month, day=current_date.day)
    return render(request, 'homepage.html', {'qs':qs})





