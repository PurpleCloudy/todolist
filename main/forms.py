from django import forms
from .models import Task

class SimpleTaskForm(forms.Form):
    month = forms.CharField(max_length=2, 
                        widget=forms.Select(choices=Task.MONTH_CHOICE),
                        default="JA",
                        verbose_name="месяц")
    day = forms.IntegerField(verbose_name="день(число)", max_value="31")
    title = forms.CharField(max_length=100)
    img = forms.ImageField(required=False)

class ComplexTaskForm(forms.Form):
    month = forms.CharField(max_length=2, 
                        widget=forms.Select(choices=Task.MONTH_CHOICE),
                        default="JA",
                        verbose_name="месяц")
    day = forms.IntegerField(verbose_name="день(число)", max_value="31")
    title = forms.CharField(max_length=100)
    body = forms.CharField()
    img = forms.ImageField(required=False)

    
class DifficultyTaskForm(forms.form):
    difficulty = forms.CharField(max_length=2,
                            widget=forms.Select(choices=Task.DIFF),
                            default='ST',
                            verbose_name="сложность")