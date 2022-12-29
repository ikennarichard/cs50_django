from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'expenses_app/index.html')


def lists(request, item):
    return render(request, 'expenses_app/list.html', {'item': item})


def notes(request, name):
    foot_note = f' <h1>Expenses App</h1> <i>Hello {name .capitalize()} Please adjust the list to suit your needs</i>'

    return HttpResponse(foot_note)