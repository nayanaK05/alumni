from django.shortcuts import render

def home(request):
    return render(request, 'portal/home.html')

def directory(request):
    return render(request, 'portal/directory.html')

def events(request):
    return render(request, 'portal/events.html')

def jobs(request):
    return render(request, 'portal/jobs.html')

