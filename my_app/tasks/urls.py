from django.urls import path
from . import views

# app_name uniquely identifies all our urls
app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task', views.add_task, name='add'),
]