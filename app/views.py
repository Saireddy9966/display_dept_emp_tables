from django.shortcuts import render
from app.models import *

def display_dept(request):
    dot=Dept.objects.all()
    d={'depts':dot}
    return render(request,'display_dept.html',context=d)

def display_emp(request):
    doe=Emp.objects.all()
    d={'empd':doe}
    return render(request,'display_emp.html',context=d)
