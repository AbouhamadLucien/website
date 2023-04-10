

# Create your models here.
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    skill_level = models.CharField(max_length=20)
    password = models.CharField(max_length=100)