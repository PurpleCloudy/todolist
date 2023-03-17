from django import forms
from .models import Task
from dataclasses import field

class ChoosingTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
                  'difficulty',
                  'date'
                  ]
        widgets = {
            'date': forms.SelectDateWidget(),
            'difficulty': forms.CheckboxInput()
        }

class SimpleTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'img',
        ]
        widgets = {
            'img':forms.ClearableFileInput()
        }

class ComplexTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'body',
            'img',
        ]
        widgets = {
            'body':forms.TextInput()
        }
