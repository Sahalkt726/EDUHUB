from django.shortcuts import render,redirect
from staff . models import *
from django.contrib.auth.decorators import login_required
from . forms import *


@login_required
def student_dashboard(request):
    student_profile = Student.objects.get(user=request.user)
    profile_image = student_profile.profile_image.url if student_profile.profile_image else None
    return render(request,'student_templates/student_dashboard.html',{'profile_image': profile_image})


def edit_student_details(request,user_id):
    user = request.user
    if request.method == 'POST':
        form = StudentChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            student = Student.objects.get(user=user)
            student.name = user.username
            student.email = user.email
            student.profile_image = user.profile_image
            student.save()
            return redirect('student_dashboard')  
    else:
        form = StudentChangeForm(instance=user)
    return render(request, 'student_templates/edit_student_details.html', {'form': form})



def student_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'student_templates/student_notifications.html', {'notifications': notifications})