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

def one_employee(request,id):
    context = {
        "employee" : Employee.objects.get(id=id)
    }
    return render(request,'one_employee.html', context)

def multiple_students(request,n):
    context = {
        "student" : Student.objects.filter(std=n)
    }
    return render(request,'mul_students.html', context)