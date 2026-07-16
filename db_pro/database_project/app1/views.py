from django.shortcuts import render
from .models import Student,Teacher

# Create your views here.

def all_students(request):
    context = {
        'Students' : Student.objects.all()
    }
    return render(request,'all_students.html', context)
