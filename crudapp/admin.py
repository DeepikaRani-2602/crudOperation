from django.contrib import admin
from crudapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','branch','rollno','city','mobileno']




admin.site.register(Student,StudentAdmin)