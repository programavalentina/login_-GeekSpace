from django.db import models
from django.core.validators import MaxValueValidator



class Student(models.Model):
    Licence = models.AutoField('Licence Student',primary_key=True)
    Name1 = models.CharField("Name", max_length=50)
    Name2 = models.CharField(max_length=50,blank=True)
    Name3 = models.CharField(max_length=50,blank=True)
    LastName1=models.CharField(max_length=50,blank=True)
    LastName2 = models.CharField(max_length=50,blank=True)
    BirthDate = models.DateField('Birth Name')
    Email = models.EmailField(max_length=80)
    Phone = models.PositiveIntegerField('Contact Phone', blank=True)



class StudentType(models.Model):
    FKLicence = models.ForeignKey(Student,on_delete=models.CASCADE)
    Description = models.TextField()

class Course(models.Model):
    IdCourse = models.AutoField(primary_key=True)
    NameCourse = models.CharField(max_length=45)
    Description = models.TextField()


class ListStudents(models.Model):
    FKIdCourse = models.ManyToManyField(Course)
    FKLicence = models.ManyToManyField(Student)

class Assistance(models.Model):
    FKLicence = models.ForeignKey(Student,on_delete=models.CASCADE)
    Estate = models.BooleanField('1 Assistence; 0 No Assistence',default=False)
