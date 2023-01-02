from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.



# django form
class NewTaskForm(forms.Form):

    task = forms.CharField(label='')




def home (request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks']
    })




def add_task (request):
    
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['task']
            request.session['tasks'] += [item]
            
            return HttpResponseRedirect(reverse('tasks:home'))
        else:
            return render(request, 'tasks/add_task.html', {
                'form': form
            })

    return render(request, 'tasks/add_task.html', {
        'form': NewTaskForm()
    })
