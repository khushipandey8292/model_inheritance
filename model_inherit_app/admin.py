from django.contrib import admin
from .models import Student,Teacher,Contractor,ExamCenter,Student1,MyExamCenter

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fees']
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','salary']
    
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','payment']
   
   
   
    
    
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']

    
@admin.register(Student1)
class Student1(admin.ModelAdmin):
    list_display=['id','cname','city','name','roll']
# Register your models here.

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']