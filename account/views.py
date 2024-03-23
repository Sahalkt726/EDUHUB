from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *


def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


def staff_signup(request):
    if request.method == 'POST':
        form = StaffSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True 
            user.save()
            
            profile_image = request.FILES.get('profile_image')
            Staff.objects.create(user=user, name=user.username, profile_image=profile_image)
            return redirect('login')  
    else:
        form = StaffSignupForm()
    return render(request, 'staff_signup.html', {'form': form})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True 
            user.save()
            profile_image = request.FILES.get('profile_image')
            Student.objects.create(user=user, name=user.username, profile_image=profile_image)

            return redirect('login')  
    else:
        form = StudentSignupForm()
    return render(request, 'student_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('staff_dashboard')
                elif user.is_student:
                    return redirect('student_dashboard')
            else:
                error_message = "Invalid username or password"
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


    


def user_logout(request):
    logout(request)
    return redirect('home')