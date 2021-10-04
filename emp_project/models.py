from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address=models.TextField(max_length=150)
    mobile = models.CharField(max_length=12)
    option1 = (("male", "male"),
               ("female", "female")
               )
    gender = models.CharField(max_length=120, choices=option1, default="male")

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)