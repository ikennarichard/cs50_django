from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item>', views.lists, name='lists'),
    path('<str:name>', views.notes, name='notes')
]