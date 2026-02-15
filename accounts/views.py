from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AlumniProfile



def home(request):
    return render(request, "accounts/home.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

         # 🔥 Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Automatically login after registration
        login(request, user)

        # Redirect to complete profile
        return redirect("complete_profile")
        

    return render(request, "accounts/register.html")

from django.contrib.auth import authenticate, login
from .models import AlumniProfile

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check if profile exists
            if not AlumniProfile.objects.filter(user=user).exists():
                return redirect("complete_profile")

            return redirect("dashboard")

    return render(request, "accounts/login.html")


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    Profile = AlumniProfile.objects.get(user=request.user)

    if not AlumniProfile.approved:
        return redirect('waiting_page')

    return render(request, "accounts/home1.html")


from .models import AlumniProfile
from django.contrib.auth.decorators import login_required

@login_required
def complete_profile(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        department = request.POST.get("department")
        passout_year = request.POST.get("passout_year")
        register_number = request.POST.get("register_number")
        phone = request.POST.get("phone")
        current_job = request.POST.get("current_job")
        company = request.POST.get("company")
        
        AlumniProfile.objects.create(
            user=request.user,
            full_name=full_name,
            department=department,
            passout_year=passout_year,
            register_number=register_number,
            phone=phone,
            current_job=current_job,
            company=company
        
        )

        return redirect("waiting")

    return render(request, "accounts/complete_profile.html")

@login_required
def waiting(request):
    return render(request, "accounts/waiting.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = AlumniProfile.objects.filter(full_name__icontains=query)

    return render(request, 'accounts/search.html', {'results': results})

@login_required
def profile(request):
    profile = AlumniProfile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})



from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm

def update_profile(request):
    profile = request.user.alumniprofile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'accounts/update_profile.html', {'form': form})










