from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks'),
    path('<str:name>', views.user_home, name='tasks'),
]