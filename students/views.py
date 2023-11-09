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
            id = request.POST.get("id")
            name = request.POST.get("name")
            age = request.POST.get("age")
            address = request.POST.get("address")
            if(id == ''):
                student = Student(name=name,age=age,address=address)
            else:
                 student = Student(id=id,name=name,age=age,address=address) 

            student.save()
            
            stddata = Student.objects.values()
            liststddata = list(stddata)
            return JsonResponse({'status':'save','stddata':liststddata})
        else:
             return JsonResponse({'status':0})  
        

def delete(request):
     if request.method == 'POST':
        id = request.POST.get("id")
        student = Student.objects.get(pk=id)
        student.delete()

        return JsonResponse({'status':1})
     else:
          return JsonResponse({'status':0})

def edit(request):
     if request.method == 'POST':
          id = request.POST.get("id")
          student = Student.objects.get(pk=id)
          stu_data = {"id":student.id,"name":student.name,"age":student.age,"address":student.address}

          return JsonResponse(stu_data)
     else:
          return JsonResponse({'status':0})
          


             