from django import forms
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from account . models import *


class StudentChangeForm(BaseUserChangeForm):
    profile_image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_image']