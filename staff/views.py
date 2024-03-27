from django.shortcuts import render,redirect,get_object_or_404
from account . models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.http import HttpResponseNotFound
from . models import *



# Create your views here.


@login_required
def staff_dashboard(request):
    staff_profile = Staff.objects.get(user=request.user)
    profile_image = staff_profile.profile_image.url if staff_profile.profile_image else None
    return render(request, 'staff_templates/staff_dashboard.html', {'profile_image': profile_image})


def manage_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.staff = request.user.staff  
            course.save()
            return redirect('manage_courses')
    else:
        form = CourseForm()
    courses = Course.objects.filter(staff=request.user.staff)
    return render(request, 'manage_course.html', {'form': form, 'courses': courses})


def delete_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        if request.method == 'POST':
            course.delete()
            return redirect('manage_courses')
    except Course.DoesNotExist:
        return HttpResponseNotFound("Course not found")
    return redirect(reverse('manage_courses'))


def update_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                return redirect('manage_courses')
        else:
            form = CourseForm(instance=course)
        return render(request, 'staff_templates/update_course.html', {'form': form})
    except Course.DoesNotExist:
        return HttpResponseNotFound("Course not found")


def create_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            students = Student.objects.all() 
            for student in students:
                Notification.objects.create(user=student.user, message=message)
            return redirect('notifications')  
    else:
        form = NotificationForm()
    return render(request, 'staff_templates/notifications.html', {'form': form})  
 






def edit_staff_details(request,user_id):
    user = request.user
    if request.method == 'POST':
        form = StaffChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            staff = Staff.objects.get(user=user)
            staff.name = user.username
            staff.email = user.email
            staff.profile_image = user.profile_image
            staff.save()
            return redirect('staff_dashboard')  
    else:
        form = StaffChangeForm(instance=user)
    return render(request, 'staff_templates/edit_staff_details.html', {'form': form})



