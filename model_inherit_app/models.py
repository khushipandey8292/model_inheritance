from django.db import models


#Abstract base table*************************************
class CommonInfo(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True
      
class Student(CommonInfo):
    fees=models.IntegerField()
    date=None
    
class Teacher(CommonInfo):
    salary=models.IntegerField()
    
class Contractor(CommonInfo):
    date=models.DateTimeField()
    payment=models.IntegerField()
    
    
 
# Multi-table inheritance****************************************** 
class ExamCenter(models.Model):
    cname=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    
class Student1(ExamCenter):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()