from django.urls import path
from . views import *

urlpatterns = [
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('student_notifications/', student_notifications, name='student_notification'),
    path('notifications/delete/<int:notification_id>/', delete_notification, name='delete_notification'),    
    path('edit_student_details/<int:user_id>/', edit_student_details, name='edit_student_details'),
    path('feedback/<int:staff_id>/', student_feedback, name='student_feedback'),
    path('questions/', display_questions, name='display_questions'),
    path('evaluate/', evaluate_answers, name='evaluate_answers'),
]
