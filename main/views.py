from django.shortcuts import render
from .forms import ChoosingTaskModelForm, SimpleTaskModelForm, ComplexTaskModelForm
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.
def choosing_diff(request):
    if request == 'POST':
        form = ChoosingTaskModelForm(request.POST)
        if form.is_valid():
            


def list_of_tasks(request, *args, **kwargs):
    current_date = datetime.now()
    qs = Task.objects.filter(month=current_date.month, day=current_date.day)
    return render(request, 'homepage.html', {'qs':qs})





