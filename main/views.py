from django.shortcuts import render
from .forms import ComplexTaskModelForm

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

