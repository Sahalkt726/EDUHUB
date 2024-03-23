from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class StaffSignupForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ['username','email']

        
class StudentSignupForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ['username', 'email']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_image','title', 'description']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
