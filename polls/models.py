from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    nombre_heure = models.IntegerField(max_length=1000)

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

class Planning(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE),
    heure = models.TimeField(auto_now=False, auto_now_add=False),
    date = models.DateField(auto_now=False, auto_now_add=False),
    lieux = models.CharField(max_length=100)

class Scretary(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

class Admin(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

