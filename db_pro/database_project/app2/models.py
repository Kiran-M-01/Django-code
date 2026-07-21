from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    desease = models.CharField(max_length=100)
    bill = models.IntegerField()
    