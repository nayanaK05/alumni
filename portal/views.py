from django.shortcuts import render

def home(request):
    return render(request, 'portal/home.html')

def directory(request):
    return render(request, 'portal/directory.html')

def events(request):
    return render(request, 'portal/events.html')

def jobs(request):
    return render(request, 'portal/jobs.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def dashboard(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(author=request.user, content=content)
        return redirect("dashboard")

    posts = Post.objects.all().order_by("-created_at")
    return render(request, "portal/dashboard.html", {"posts": posts})

