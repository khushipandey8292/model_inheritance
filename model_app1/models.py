from django.db import models
from .managers import CustomManager
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()

    # students=models.Manager()
    students=CustomManager()
    objects=CustomManager()