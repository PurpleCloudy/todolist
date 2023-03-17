from django.shortcuts import render
from .forms import ChoosingTaskModelForm, SimpleTaskModelForm, ComplexTaskModelForm
from .models import Task
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime

# Create your views here.
def choosing_diff(request):
    if request == 'POST':
        form = ChoosingTaskModelForm(request.POST or None)
        if form.is_valid():
            diff = form.cleaned_data.get('difficulty')
            date = form.cleaned_data.get('date')
            return HttpResponseRedirect(reverse('simple_task'))
    else:
        form = ChoosingTaskModelForm()
    return render(request, '') 

def simpletask_view(request, *args, **kwargs):
    pass

def list_of_tasks(request, *args, **kwargs):
    current_date = datetime.now()
    qs = Task.objects.filter(month=current_date.month, day=current_date.day)
    return render(request, 'homepage.html', {'qs':qs})





