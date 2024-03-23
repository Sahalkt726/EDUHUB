from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_image=models.ImageField(upload_to='staff_profile/', blank=True)

    def __str__(self):
        return self.name
       

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_image=models.ImageField(upload_to='student_profile/', blank=True)


    def __str__(self):
        return self.name
    

class Course(models.Model):
    course_image=models.ImageField(upload_to='Course_images/')
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=250)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)

    def __str__(self):
        return self.title