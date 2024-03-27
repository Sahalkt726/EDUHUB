from django.urls import path
from . views import *

urlpatterns = [
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('student_notifications/', student_notifications, name='student_notification'),
    path('edit_student_details/<int:user_id>/', edit_student_details, name='edit_student_details'),
]
