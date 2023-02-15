from django.shortcuts import render
from .forms import ComplexTaskModelForm
from .models import Task

# Create your views here.
def choosing_diff(request, *args, **kwargs):
    if request.method == "POST":
        form = ComplexTaskModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = ComplexTaskModelForm()
            return render(request, 'forms.html', {'form':form, 'obj':obj})
    form = ComplexTaskModelForm(request.POST or None)
    return render(request, 'forms.html', {'form':form})

def homepage(request, *args, **kwargs):
    qs = Task.objects.all()
    date = True
    if qs == []:
        return render(request, 'homepage.html', {'qs':qs, 'date':date})
    return render(request, 'homepage.html', {'qs':qs, 'date':date})

