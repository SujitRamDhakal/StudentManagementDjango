from django.shortcuts import render,redirect
from .models import Student
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

def index(request):

    students = Student.objects.all()
    context = {
        'students':students,
    }

    return render(request,'index.html',context)

# @csrf_exempt
def save(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            age = request.POST.get("age")
            address = request.POST.get("address")

            student = Student(name=name,age=age,address=address)
            student.save()
            stddata = Student.objects.values()
            liststddata = list(stddata)
            return JsonResponse({'status':'save','stddata':liststddata})
        else:
             return JsonResponse({'status':0})  
             