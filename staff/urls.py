from django.urls import path
from .views import *

urlpatterns = [
    # path('staff_dashboard/', staff_dashboard, name='staff_dashboard'),
    path('manage-courses/', manage_courses, name='manage_courses'),
    path('delete-course/<int:course_id>/', delete_course, name='delete_course'), 
    path('update-course/<int:course_id>/', update_course, name='update_course'),
    path('notifications/', create_notification, name='notifications'),
    path('edit_staff_details/<int:user_id>/', edit_staff_details, name='edit_staff_details'),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
