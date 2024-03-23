from django import forms
from account . models import *
from . models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_image', 'title', 'description']


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message']


class StaffEditForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'profile_image'] 

