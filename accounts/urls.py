from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('waiting/', views.waiting, name='waiting'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),




]

