from django.contrib import admin
from .models import Student

admin.site.register(Student)
# to display what the function returns in the model


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id','name','age','address')


# to display all the fields in the list 