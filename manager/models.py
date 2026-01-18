from django.db import models

# Create your models here.

class Roles(models.Model):
    name = models.CharField(max_length=25)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey(Roles, on_delete=models.PROTECT)