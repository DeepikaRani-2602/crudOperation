from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    branch=models.CharField(max_length=300)
    rollno=models.IntegerField()
    city=models.CharField(max_length=50)
    mobileno=models.IntegerField()