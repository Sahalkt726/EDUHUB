from django.shortcuts import render
from staff . models import *
from django.contrib.auth.decorators import login_required


@login_required
def student_dashboard(request):
    student_profile = Student.objects.get(user=request.user)
    profile_image = student_profile.profile_image.url if student_profile.profile_image else None
    return render(request,'student_dashboard.html',{'profile_image': profile_image})


def student_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'student_notifications.html', {'notifications': notifications})