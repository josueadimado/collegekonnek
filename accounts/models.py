from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Student(CustomUser):
    gender = models.CharField(max_length=50,null=True)
    career = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.username