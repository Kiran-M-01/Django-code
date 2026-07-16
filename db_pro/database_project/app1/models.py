from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    std = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)

class Employee(models.Model):
    ename = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    salary = models.IntegerField()
    deptno = models.IntegerField()

    