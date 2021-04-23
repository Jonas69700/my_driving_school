from django.db import models
from datetime import datetime, date

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    tel = models.CharField(max_length=12)
    nombre_heure = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
       return 'Student: {} : {} '.format(self.id, self.name)

class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    tel = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
       return 'Instructor: {} : {} '.format(self.id, self.name)

class Planning(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    date_rdv= models.DateField(auto_now_add=False, auto_now=False, blank=True)
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
       return 'Planning: {}, date: {} {}, student: {}'.format(self.id, self.date_rdv, self.hour, self.student.name)

class Secretary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    tel = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
       return 'Secretary: {} : {} '.format(self.id, self.name)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
       return 'Admin: {} : {} '.format(self.id, self.name)

