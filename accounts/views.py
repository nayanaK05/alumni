from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request, "accounts/home.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("register")

    return render(request, "accounts/register.html")

from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})

    return render(request, "accounts/login.html")

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")



