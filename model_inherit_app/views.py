from django.shortcuts import render
from .models import Student,Teacher,Contractor,Student1,ExamCenter
def home(request):
    # student_data=Student.objects.all()
    # teacher_data=Teacher.objects.all()
    # contractor_data=Contractor.objects.all()
    # return render(request,'home.html',{'students':student_data,'teachers':teacher_data,'contractors':contractor_data})

    student_data=Student1.objects.all()
    examcenter_data=ExamCenter.objects.all()
    return render(request,'home.html',{'student1s':student_data,'examcenters':examcenter_data})
    
      