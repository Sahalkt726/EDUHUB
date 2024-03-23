from django.urls import path
from . views import *

urlpatterns = [
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('student_notifications/', student_notifications, name='student_notification'),
]
