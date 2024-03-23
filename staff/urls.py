from django.urls import path
from .views import *

urlpatterns = [
    path('staff_dashboard/', staff_dashboard, name='staff_dashboard'),
    path('manage-courses/', manage_courses, name='manage_courses'),
    path('delete-course/<int:course_id>/', delete_course, name='delete_course'), 
    path('update-course/<int:course_id>/', update_course, name='update_course'),
    path('notifications/', create_notification, name='notifications'),
    path('edit-staff-details/', edit_staff_details, name='edit_staff_details'),
]