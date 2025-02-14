from django.shortcuts import render
from .models import Student
# Create your views here.
def model_manager(request):
    # student_data=Student.students.all()
    # student_data=Student.objects.all()
    student_data=Student.objects.get_stu_roll_range(111,113)
    return render(request,'about_manager.html',{'students':student_data}) 