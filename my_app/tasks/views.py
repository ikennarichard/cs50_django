from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'tasks/index.html', {
        'task': True,
        'task1': 'Buy Groceries'
})


def user_home (request, name):
    return render(request, 'tasks/index.html', {
        'name': name.capitalize(),
        'task': True,
        'task1': 'Buy Groceries'
    })
