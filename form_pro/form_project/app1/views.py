from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo
# Create your views here.

def info(request):
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

    obj = UserInfo.objects.create(name=name,age=age,gender=gender)

    return HttpResponse(f"{name}'s informatons added successfully")
        