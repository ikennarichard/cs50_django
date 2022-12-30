from django import forms
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

# django form
class NewTaskForm(forms.Form):
    task = forms.CharField()
    priority = forms.IntegerField(min_value=1, max_value=5)

def home (request):
    return render(request, 'tasks/index.html')


def add_task (request):
    return render(request, 'tasks/add_task.html', {
        'form': NewTaskForm()
    })
