from django import forms
from .models import Task
from dataclasses import field

class ComplexTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
                  'difficulty',
                  'month',
                  'day', 
                  'title', 
                  'body', 
                  'file'
                  ]