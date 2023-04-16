from django.db import models

# Create your models here.

class Dept(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=200)
    loc=models.CharField(max_length=100)

class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=50)
    Mgr=models.IntegerField()
    Hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(null=True)
    Dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    
