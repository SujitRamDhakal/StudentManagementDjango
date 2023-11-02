from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student

def index(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        address = request.POST.get("address")

        student = Student.objects.create(name=name,age=age,address=address)
        student.save()
        return redirect('/index/')

    students = Student.objects.all()
    context = {
        'students':students,
    }

    return render(request,'index.html',context)
