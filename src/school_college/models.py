from django.db import models
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')

class Parents(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')

class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    is_present = models.BooleanField(default=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    parents = models.ForeignKey(Parents, on_delete=models.CASCADE)
