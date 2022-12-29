from django.shortcuts import render
import datetime

# Create your views here.

def index(request, name):
    now = datetime.datetime.now()
    return render(request, 'new_year/new_year.html', {
    'name': name.capitalize(),
    'newyear': now.month == 1 and now.day == 1 
    })