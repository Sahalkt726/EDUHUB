from django.db import models
from account . models import *

# Create your models here

class Feedback(models.Model):
    staff_member = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField() 

    def __str__(self):
        return self.message

