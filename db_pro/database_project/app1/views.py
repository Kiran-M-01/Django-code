from django.shortcuts import render
from .models import Student,Teacher,Employee

# Create your views here.

# FOR STUDENT TABLE
def all_students(request):
    context = {
        'Students' : Student.objects.all()
    }
    return render(request,'all_students.html', context)


# FOR EMPLOYEE TABLE
def all_employees(request):
    context = {
        "Employees" : Employee.objects.all()
    }
    return render(request,'all_employees.html', context)