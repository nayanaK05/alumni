from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('directory/', views.directory, name='directory'),
    path('events/', views.events, name='events'),
    path('jobs/', views.jobs, name='jobs'),
]
