from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='home'),
    path('student_signup/', student_signup, name='student_signup'),
    path('staff_signup/', staff_signup, name='staff_signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)