from django.contrib import admin
from .models import Employee

# Register your models here.

@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display = ['id','ename','salary']

# admin.site.register(Employee,EmployeeModel)

