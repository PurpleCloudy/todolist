from django.shortcuts import render
from .forms import SimpleTaskForm, ComplexTaskForm, DifficultyTaskForm

# Create your views here.
def choosing_diff(request, *args, **kwargs):
    if request.method == "POST":
        form = DifficultyTaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = DifficultyTaskForm()
            return render(request, 'difficulty.html', {'form':form, 'obj':obj})
    form = DifficultyTaskForm(request.POST or None)
    return render(request, 'forms.html', {'form':form})

# def create_view(request, *args, **kwargs):
#     if request.method == "POST":
#        form = NewsModelForm(request.POST, request.FILES)
#        if form.is_valid():
#            obj = form.save(commit=False)
#            obj.author = request.user
#            obj.save()
#            form = NewsModelForm()
#            return render(request, 'forms.html', {'form':form, 'obj':obj})
#     form = NewsModelForm(request.POST or None)
#     return render(request, 'forms.html', {'form':form})