from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=50)

class CustomUser(AbstractUser):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
